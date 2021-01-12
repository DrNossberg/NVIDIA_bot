#!/usr/bin/env python
# -*- coding: utf-8 -*-


PAGE_URL= 0
STATUS  = 1

class Card(object):
    """docstring for Card"""
    def __init__(self, name, url, status = 1):
        super(Card, self).__init__()
        self.name = name
        self.pages = [[url, status]]
        self.actual = 0
        self.dic = {0 : "BANNED FROM URL", 1: "OUT OF STOCK", 2 : "EN STOCK"}

    def get_name(self):
        return (self.name)

    def add_url(self, url):
        self.pages.append([url, 1])

    def get_url(self, nbr = -1):
        if (nbr != -1):
            self.actual = nbr
        return (self.pages[self.actual][PAGE_URL])

    def set_status(self, status):
        self.pages[self.actual][STATUS] = status

    def get_status(self, nbr = -1):
        if (nbr != -1):
            self.actual = nbr
        return (self.pages[self.actual][STATUS])

    def next(self):
        self.actual += 1
        if (self.actual >= len(self.pages)):
            self.actual = 0

    def dump(self):
        print(self.name + " :\n\t", "\n\t".join("{0}".format(page) for page in self.pages), sep='')
