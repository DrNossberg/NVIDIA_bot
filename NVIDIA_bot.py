#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
import time
import datetime 


############### Variables à modifier vous même ######################


PrixCG          = -1    #    Le max que vous soyez prêt à mettre. Laissez -1 pour tout voir
seeked_GPU      = [2]    #    0 = 3060, 1 = 3070, 2 = 3080, 3 = 3090.                   Si vous voulez tout voir laisser vide
manufacturer      = []    #    marque que vous recherchez (site LDLC).                 Si vous voulez tout voir laisser vide
                        #       ex : Je veux que FE et Gainward :
                        #            = ["NVIDIA", "Gainward"]

############### Debut du code ######################

available = 0
FE_list = [[1, "3060 Ti", "https://www.ldlc.com/fiche/PB00036063.html"],
            [2, "3070",    "https://www.ldlc.com/fiche/PB00036064.html"],
            [3, "3080",    "https://www.ldlc.com/fiche/PB00033884.html"],
            [4, "3090",    ""]]

pretty_gpu_liste = "&gpu="          + ",".join( FE[1] for FE in FE_list if i in seeked_GPU or seeked_GPU == [])
brand_selection  = "" if manufacturer == [] else "&manufacturer=" + ','.join(manufacturer)
NVIDIA_URL = "https://www.nvidia.com/fr-fr/shop/geforce/gpu/?page=1&limit=9&locale=fr-fr&category=GPU" + pretty_gpu_liste + brand_selection

LDLC_URL = "https://www.ldlc.com/recherche/{GPU}/+fcat-4684.html?department=all".replace("{GPU}", FE_list[seeked_GPU[0] if seeked_GPU != [] else 0][1])

def display_ban_ip():
    print("Ban \033[31mip\033[0m ou timeout... désolé!")
    exit()

def ping_FE():
    stock = 0

    for FE in FE_list[:-1]:
        if FE[0] in seeked_GPU :
            status_code = requests.get(FE[2]).status_code
            if status_code == 200 :
                print("\033[32m" + FE[1] + "EN STOCK! :\033[0m ici : " + FE[2])
                print(datetime.datetime.utcnow().strftime("%H:%M:%S"))
                stock = 1
            if status_code in [404, 410] :
                continue
            else :
                display_ban_ip()
    if stock == 1:
        return (True)
    return (False)

def scrap_nvidia() :
    return (False)

def scrap_ldlc() :
    r = requests.get(LDLC_URL)
    print ("Refreshed !")

    if r.status_code != 200:
        display_ban_ip()

    soup = BeautifulSoup(r.content,"html.parser")
    for item in soup.findAll('div', {"class": "listing-product"})[0].findAll('li', id=lambda x: x and x.startswith("pdt-")):
        try:
            Stock = re.findall(r'Web\n(.*)', str(item.text))[0]
            if Stock == 'En stock' or 'Entre' in Stock :
                available = 1
        except:
            Stock = "Pas En Stock" #// est-ce qu'on à besoin de ça ? 
        try:
            Prix2 = re.findall(r'(.*)€(.*)',str(item.text))[0] ## Casse couille avec les valeurs > 1000€. Retrait de la valeur 'espace' traduit avec le cul par BeautifulSoup
            try:
                Prix = '%s€%s'%Prix2
                PrixMin = int(Prix2[0])
            except:
                PrixTemps = Prix2[0].split('\xa0') # '\xao0' représente la valeur espace
                PrixTempsf = PrixTemps[0] + PrixTemps[1]
                Prix = '%s€%s'%(PrixTempsf, Prix2[1])
                PrixMin = int(PrixTempsf)
        except:
            print("ça merde")
            continue

        item_name = item.find('h3').get_text()

        if available and (brand_list == [] or item_name[0:item_name.find(' ')] in brand_list) and (PrixMin <= PrixCG or PrixCG < 0) :
            print("\033[32mEN STOCK! :\033[0m")
            print(item_name, Stock, Prix)
            print(datetime.datetime.utcnow().strftime("%H:%M:%S"))
            return (True) #ce qui serait super cool ce serait de mettre la fiche du produit, que la personne puisse y accéder direct en CTRL + click. T'aurais pas à refresh au moment ou les server sont surchargés
    return (False)


if __name__ == "__main__":
    print (LDLC_URL)
    print (NVIDIA_URL)
    print ("Looking for", pretty_gpu_liste)

    while True:
        if scrap_ldlc() or scrap_nvidia() or ping_FE():
            exit()
        time.sleep(8)
