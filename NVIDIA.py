#!/usr/bin/env python
# -*- coding: utf-8 -*-


class NVIDIA(object):
    """docstring for NVIDIA"""
    def __init__(self, FE_list, brand_list):
        super(NVIDIA, self).__init__()
        self.NVIDIA_URL = "https://www.nvidia.com/fr-fr/shop/geforce/gpu/?page=1&limit=9&locale=fr-fr&category=GPU"
            + "&gpu="          + ",".join([FE[0] for FE in FE_list])
            + "" if manufacturer == [] else "&manufacturer=" + ','.join(manufacturer)
        
def scrap_nvidia() :
    return (False)
