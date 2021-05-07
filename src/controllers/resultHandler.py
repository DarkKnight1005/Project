# Transfered into the filterService
from src.models import *

class ResultHandler:
    def __init__(self, ls_all):
        self.__ls_all = ls_all

    def handle(self):
        ls_amazon = []
        ls_tapaz = []
        
        for elem in self.__ls_all:
            if elem.shopName == "amazon":
                ls_amazon.append(elem)
            elif elem.shopName == "tapaz":
                ls_tapaz.append(elem)

        return ls_amazon, ls_tapaz