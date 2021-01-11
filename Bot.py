#!/usr/bin/env python
# -*- coding: utf-8 -*-


# import platform
# import json
# from time import sleep
# import random
# import webbrowser
# from datetime import datetime, time
# from os import path, getenv, system
# from urllib.request import urlopen, Request

from Discord    import alert
# from NVIDIA     import *
from LDLC       import *
from Card import Card

############### Variables à modifier vous même ######################


PrixCG          = -1    #    Le max que vous soyez prêt à mettre. Laissez -1 pour tout voir
seeked_GPU      = []    #   0 = 3060, 1 = 3070, 2 = 3080, 3 = 3090.                   Si vous voulez tout voir laisser vide
manufacturer    = []    #    marque que vous recherchez (site LDLC).                 Si vous voulez tout voir laisser vide
                        #       ex : Je veux que FE et Gainward :
                        #            = ["NVIDIA", "Gainward"]

############### Debut du code ######################

available = 0
FE_list =  [Card("3060 Ti", "https://www.ldlc.com/fiche/PB00036063.html"),
            Card("3070",    "https://www.ldlc.com/fiche/PB00036064.html"),
            Card("3080",    "https://www.ldlc.com/fiche/PB00033884.html"),
            Card("3090",    "", 0)]

FE_list = [ FE_list[i] for i in range(0, len(FE_list)) if i in seeked_GPU or seeked_GPU == []]


if __name__ == "__main__":


    alert(['Connecting...'])
    # alerte(["Looking for", ",".join([FE[0] for FE in FE_list])])

    LDLC(FE_list, manufacturer)
    for FE in FE_list :
        FE.dump()
    # print(FE_list)
    # print("here", FE_list)
    # while True:
    #     if scrap_ldlc() or scrap_nvidia() or ping_FE():
    #     time.sleep(8)
