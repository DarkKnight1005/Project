from .filter import *
from src.models import *

class PriceLessThan(Filter):
    
    def __init__(self, price_to):
        self.__price_to = price_to
    
    def applyFilter(self, ls_all):
        if self.__price_to == None:
            self.__price_to = 100000000
        
        _ls_temp = []
        for elem in ls_all:
            if elem.price != "---" and elem.price.find('price') == -1 and elem.price.find(",") == -1  and float(elem.price[:-1]) <= int(self.__price_to):
                _ls_temp.append(elem)  
        ls_all = _ls_temp[:]
        return ls_all