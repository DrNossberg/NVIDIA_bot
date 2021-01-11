#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

# from Discord import *


class LDLC(object):
    """check pour :
        - des drop de cartes sur la recherche 
        - des FE sur les pages produits de celles-ci """
    def __init__(self, FE_list, manufacturer):
        super(LDLC, self).__init__()
        LDLC_URL = "https://www.ldlc.com/recherche/{GPU}/+fcat-4684.html?department=all"
        for FE in FE_list:
            FE.add_url(LDLC_URL.replace("{GPU}", FE.name))
        # return (FE)


    # def search_gpu(self):
    #     """0 : indisponible, 1 : ban, 2 : dispo"""
    #     for node in self.LDLC_URLS:
    #         if (node[1][0] != 1) :
    #             node[1][0] = scrap_search_one_gpu(node[0])
    #             if node[1][0] == 2 : 
    #                 alert([node[0] + "EN STOCK!" + "ici : ", node[0]])
    #                 node[1][0] 

    #     for node in self.FE_list:
    #         if (node[2] != 0) :
    #             node[2] = scrap_search_one_gpu(node[1])
    #         if node[1] == 2 : 
    #             alert([node[0] + "EN STOCK!" + "ici : ", node[1]])


    # def scrap_search_one_gpu(self, url):
    #     r = requests.get(url)

    #     if r.status_code != 200:
    #         return (1)


    #     soup = BeautifulSoup(r.content,"html.parser")
    #     for item in soup.findAll('div', {"class": "listing-product"})[0].findAll('li', id=lambda x: x and x.startswith("pdt-")):
    #         try:
    #             Stock = re.findall(r'Web\n(.*)', str(item.text))[0]
    #             if Stock == 'En stock' or 'Entre' in Stock :
    #                 available = 1
    #         except:
    #             pass
    #         try:
    #             Prix2 = re.findall(r'(.*)€(.*)',str(item.text))[0] ## Casse couille avec les valeurs > 1000€. Retrait de la valeur 'espace' traduit avec le cul par BeautifulSoup
    #             try:
    #                 Prix = '%s€%s'%Prix2
    #                 PrixMin = int(Prix2[0])
    #             except:
    #                 PrixTemps = Prix2[0].split('\xa0') # '\xao0' représente la valeur espace #TODO // bruh
    #                 PrixTempsf = PrixTemps[0] + PrixTemps[1]
    #                 Prix = '%s€%s'%(PrixTempsf, Prix2[1])
    #                 PrixMin = int(PrixTempsf)
    #         except:
    #             print("ça merde")
    #             continue

    #         item_name = item.find('h3').get_text()

    #         if available and (brand_list == [] or item_name[0:item_name.find(' ')] in brand_list) and (PrixMin <= PrixCG or PrixCG < 0) :
    #             return (2)
    #             #ce qui serait super cool ce serait de mettre la fiche du produit, que la personne puisse y accéder direct en CTRL + click. T'aurais pas à refresh au moment ou les server sont surchargés
    #     return (0)

    # def ping_FE(url):
    #     status_code = requests.get(FE[1]).status_code
    #     if status_code == 200 :
    #         return (2)
    #     if status_code in [404, 410] :
    #         return (0)
    #     else :
    #         return (1)
    #     return (0)




# def Func404(String_url):
#     r = requests.get(String_url)
#     print(r)
#     if '404' in str(r) or '410' in str(r):
#         PasDeStockFE=0
#     elif '200' in str(r):
#         PasDeStockFE=1
#     else:
#         print('Désolé.. Ban IP! Timeout à revoir')
#         PasDeStockFE=0
#     return PasDeStockFE


#     def FuncPourBotFE():
#     JeVeux=0 # 3060TI
#     PasDeStockFE=0
#     ############### Debut du code ######################
#     String_url=r'https://www.ldlc.com/fiche/PB00036063.html' #3060TI
#     String_url2=r'https://www.ldlc.com/fiche/PB00036064.html' #3070
#     String_url3=r'https://www.ldlc.com/fiche/PB00033884.html' #3080
#     PasDeStockFE3060=Func404(String_url)
#     sleep(1)
#     PasDeStockFE3070=Func404(String_url2)
#     sleep(1)
#     PasDeStockFE3080=Func404(String_url3)
#     if PasDeStockFE3060==1 :
#         PasDeStockFE=1
#     if PasDeStockFE3070==1:
#         PasDeStockFE=1
#     if PasDeStockFE3080==1:
#         PasDeStockFE=1
#     return PasDeStockFE3060,PasDeStockFE3070,PasDeStockFE3080



#    PasDeStockFE3060,PasDeStockFE3070,PasDeStockFE3080=FuncPourBotFE()
#             if PasDeStockFE3060==1 and PasDeStockFE3060Avant==0:
#                 PasDeStockFE3060Avant=1
#                 alert(["Y A DU STOCK DE 3060 FE!!!!",'https://www.ldlc.com/fiche/PB00036063.html'])
#             elif PasDeStockFE3060==0 and PasDeStockFE3060Avant==1:
#                 PasDeStockFE3060Avant=0
#                 alert(["Fin du drop pour les 3060 FE! ",':hap:'])

#             if PasDeStockFE3070==1 and PasDeStockFE3070Avant==0:
#                 PasDeStockFE3070Avant=1
#                 alert(["Y A DU STOCK DE 3070 FE!!!!",'https://www.ldlc.com/fiche/PB00036064.html'])
#             if PasDeStockFE3070==0 and PasDeStockFE3070Avant==1:
#                 PasDeStockFE3070Avant=0
#                 alert(["Fin du drop pour les 3070 FE! ",':hap:'])

#             if PasDeStockFE3080==1 and PasDeStockFE3080Avant==0:
#                 PasDeStockFE3080Avant=1
#                 alert(["Y A DU STOCK DE 3080 FE!!!!",'https://www.ldlc.com/fiche/PB00033884.html'])
#             if PasDeStockFE3080==0 and PasDeStockFE3080Avant==1:
#                 PasDeStockFE3080Avant=0
#                 alert(["Fin du drop pour les 3080 FE! ",':hap:'])

#             ################### Partie LDLC master race
#             FullContent0=FuncPourBotLDLC()
#             # AFinir=0
#             for i in FullContent0:
#                 if i==0: # 3070
#                     if len(FullContent0[i])>0 and len(LDLC3070)==0:
#                         alert(["Y a du stock de 3070 sur LDLC!!",' https://www.ldlc.com/recherche/3070/+fcat-4684.html?department=all'])
#                         LDLC3070=[1]
#                     elif len(FullContent0[i])>0 and len(LDLC3070)>0:
#                         alert(["Fin du stock de 3070 sur LDLC",' :hap:'])
#                         LDLC3070=[]
#                 elif i==1: # 3060
#                     if len(FullContent0[i])>0 and len(LDLC3060)==0:
#                         alert(['y a du stock de 3060 sur LDLC!!',' https://www.ldlc.com/recherche/3060/+fcat-4684.html?department=all'])
#                         LDLC3060=[1]
#                     elif len(FullContent0[i])>0 and len(LDLC3060)>0:
#                         alert(["Fin du stock de 3060 sur LDLC",' :hap:'])
#                         LDLC3060=[]
#                 elif i==2: #3080
#                     if len(FullContent0[i])>0 and len(LDLC3080)==0:
#                         alert(['y a du stock de 3080 sur LDLC!!',' https://www.ldlc.com/recherche/3080/+fcat-4684.html?department=all'])
#                         LDLC3080=[1]
#                     elif len(FullContent0[i])>0 and len(LDLC3080)>0:
#                         alert(["Fin du stock de 3080 sur LDLC",' :hap:'])
#                         LDLC3080=[]





