#!/usr/bin/env python
# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup

from Discord import *
from Card import Card

PCC_search_link    = 2


class PCComponents(object):
    """docstring for PCComponents"""
    def __init__(self, Card_list, manufacturer):
        super(PCComponents, self).__init__()
        PCC_URL ='https://www.pccomponentes.com/tarjetas-graficas/geforce-rtx-{GPU}-series'
        for FE in Card_list:
            FE.add_url(PCC_URL.replace("{GPU}", FE.name[0:4]))
        self.Card_list = Card_list
        self.brand_list = manufacturer
        self.card_dispo = {}

    def scrap_search_gpu(self, FE):
        req = requests.get(FE.get_url(PCC_search_link))
        if req.status_code != 200:
            FE.set_status(0) # banned ou timed out
            return
    
        for item in BeautifulSoup(req.content,'html.parser').find('div', id='articleListContent').findAll('a', {'class':'GTM-productClick enlace-superpuesto cy-product-hover-link'}):
            item_name = str(item["data-name"])
            if item["data-stock-web"] in ['4', '9999'] or "Reacondicionado" in item_name:
                if item_name in self.card_dispo : # no longer available
                    self.card_dispo[item_name].set_status(1)
                    del self.card_dispo[item_name]
                continue
            prix = float(item["data-price"])
            # if prix < prixMax : ? faudrais faire un tableau de sa, avec prix max pour chaque carte
            # brand ? extraire la brand du nom de la carte
            
            if item_name not in self.card_dispo :
                self.card_dispo[item_name] = Card(item_name, "https://www.pccomponentes.com" + str(item['href']), 2, str(prix)) #just entered in stock !
                continue
            # r2 = requests.get(LienHyperText,timeout=(3.05, 27))
                # soup2 = BeautifulSoup(r2.content,'html.parser')
                # Search33=soup2.findAll('button', id='notify-me')
                # Search38=soup2.findAll('div', {'class':'ficha-producto__acciones white-card-movil hidden-sm-down'})
                # print(Search38)
                # if len(Search33)==0:
