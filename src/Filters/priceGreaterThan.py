from .filter import *

class PriceGreaterThan(Filter):
    
    def __init__(self, price_from):
        self.__price_from = price_from
    
    def applyFilter(self, ls_all):
        if self.__price_from == None:
            price_from = 0

        _ls_temp = []
        for elem in ls_all:
            if elem[1] != "---" and elem[1].find('price') == -1 and elem[1].find(",") == -1 and float(elem[1][:-1]) >= int(self.__price_from):
                _ls_temp.append(elem)  
        ls_all = _ls_temp[:]
        return ls_all