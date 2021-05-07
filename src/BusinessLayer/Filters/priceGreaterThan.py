from .filter import *
from src.models import *

class PriceGreaterThan(Filter):
    
    def __init__(self, price_from):
        self.__price_from = price_from
    
    def applyFilter(self, ls_all):
        if self.__price_from == None:
            price_from = 0

        _ls_temp = []

        print(self.__price_from)

        for elem in ls_all:
            if elem.price != "---" and elem.price.find('price') == -1 and elem.price.find(",") == -1 and float(elem.price[:-1]) >= int(self.__price_from):
                _ls_temp.append(elem)  
        ls_all = _ls_temp[:]
        return ls_all