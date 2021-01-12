#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from time import sleep
import requests
import re

from Discord import *
from Card import Card


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
        self.card_dispo = {}


    def ping_FE_page(self, FE):
        """check chaque page founder de LDLC"""
        status_code = requests.get(FE.get_url(LDLC_FE_link)).status_code
        if status_code == 200 :
            if FE.get_status() != 2 :
                alert(FE.name + "FE disponible ! Ici :" + FE.get_url(LDLC_FE_link)) # alerte en double.
                FE.set_status(2) # in stock
            return
        if status_code in [404, 410] :
            if FE.get_status() == 2 :
                alert("Fin du stock pour la" + FE.name + "FOUNDER EDITION") # pareil
                FE.set_status(1) # Out of stock
            return
        FE.set_status(0) # banned


    def scrap_search_gpu(self, FE):
        """check la recherche de LDLC
         on fait un dico avec toutes les cartes disponibles. self.card_dispo["nom de la carte"] = Objet Card
        dès qu'une carte n'est plus dispo, elle est retirée du dico. Simple, on peut gérer autant de cartes que l'on vaut"""
        req = requests.get(FE.get_url(LDLC_search_link))
        if req.status_code != 200:
            FE.set_status(0) # banned ou timed out
            return

        for item in BeautifulSoup(req.content,"html.parser").find('div', {"class": "listing-product"}).findAll('li'):
            line = item.find('h3').find('a') 
            item_name = item.find('h3').get_text()
            item_brand = item_name.split(' ')[0]

            if self.brand_list != [] and item_brand not in self.brand_list: # 'not in' => !/ perfs \!
                continue
            try:
                if re.search(r"Web\n(.*)", item.text).group(1) != "Rupture" and item_name not in self.card_dispo: # available
                    self.card_dispo[item_name] = (Card(item_name, "https://www.ldlc.com" + line['href'], 2, 
                    str(re.search(r"(.*)€(.*)", item.text).group(0))))  # in stock
                    continue
                    # maybe useless                       maybe this only do the trick
                if item_name in self.card_dispo and self.card_dispo[item_name].get_status() == 2 : # no longer available 
                    self.card_dispo[item_name].set_status(1)
                    del self.card_dispo[item_name]
            except Exception as e:
                print(e)
