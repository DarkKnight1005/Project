from .filter import *

class AndFilter(Filter):

    def __init__(self, filter1, filter2):
        self.__filter1 = filter1
        self.__filter2 = filter2

    def applyFilter(self, ls_all):
        _ls_all = self.__filter1.applyFilter(ls_all)
        _ls_all = self.__filter2.applyFilter(ls_all)
        
        return _ls_all