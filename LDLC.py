#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from time import sleep
import requests
import re

from Discord import *


LDLC_FE_link        = 0
LDLC_search_link    = 1


class LDLC(object):
    """check pour :
        - des drop de cartes sur la recherche 
        - des FE sur les pages produits de celles-ci """
    def __init__(self, Card_list, manufacturer):
        super(LDLC, self).__init__()
        LDLC_URL = "https://www.ldlc.com/recherche/{GPU}/+fcat-4684.html?department=all"
        for FE in Card_list:
            FE.add_url(LDLC_URL.replace("{GPU}", FE.name))
        self.Card_list = Card_list
        self.brand_list = manufacturer
        self.card_dispo = []

    def search_GPU(self):
        """Pour chaque card dans la liste de cartes 30XX, on check les 
        pages Founder puis la recherche LDLC"""
        for FE in self.Card_list:
            if FE.get_status(LDLC_FE_link) != 0 :
                self.ping_FE_page(FE)
            sleep(1)
            if FE.get_status(LDLC_search_link) != 0 :
                self.scrap_search_gpu(FE)
            sleep(10)

    def ping_FE_page(self, FE):
        """check chaque page founder de LDLC"""
        status_code = requests.get(FE.get_url(LDLC_FE_link)).status_code
        if status_code == 200 :
            if FE.get_status() != 2 :
                alert(FE.name + "FE disponible ! Ici :" + FE.get_url(LDLC_FE_link))
                FE.set_status(2) # in stock
            return
        if status_code in [404, 410] :
            if FE.get_status() == 2 :
                alert("Fin du stock pour la" + FE.name + "FOUNDER EDITION")
                FE.set_status(1) # Out of stock
            return
        FE.set_status(0) # banned


    def scrap_search_gpu(self, FE):
        """check la recherche de LDLC"""
        req = requests.get(FE.get_url(LDLC_search_link))
        if req.status_code != 200:
            FE.set_status(0) # banned

        soup = BeautifulSoup(req.content,"html.parser")


        # .string
        for item in soup.find('div', {"class": "listing-product"}).findAll('li'):
            # print(item.find('Web').get_text())
            try:
                if re.search(r"Web\n(.*)", item.text).group(1) != "Rupture" :
                    FE.set_status(2) # in stock
                elif FE.get_status() == 2 :
                    alert("Fin du stock pour la" + FE.name)
                    FE.set_status(1)
            except Exception as e:
                print(e)
                continue
            try:
                prix = str(re.search(r"(.*)€(.*)", item.text).group(0))
            except Exception as e:
                print(e)
                continue


            line = item.find('h3').find('a') 
            item_name = item.find('h3').get_text()
            item_brand = item_name.split(' ')[0]
            if FE.get_status() == 2 and (self.brand_list == [] or item_brand in self.brand_list) :
                # self.card_dispo.append(item_name)
                alert(FE.name + "Carte disponible ! Dans la recherche ici :" + 
                    line['href'] )

        # mieux gérer ici, genre un tableau dans le tableau ou une merde du genre,
        # tableau dans les cards ou je sais pas ou ici, pareil pr PCComponent

        # améliorer le truc pour avoir le name en 1er, puis la dispo, puis le prix et enfin le save


# a href="/fiche/