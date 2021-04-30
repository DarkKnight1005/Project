from .filter import *

class ShippingFilter(Filter):
    def __init__(self):
        pass
    
    def applyFilter(self, ls_all):
        _nonShipable = []
        _shipable = []
        for elem in ls_all:
            if elem[1] == "---":
                _nonShipable.append(elem)
            else:
                _shipable.append(elem)
        ls_all = _nonShipable[:]
        ls_all.extend(_shipable)
        return ls_all