from src.Filters import *

class FilterService:
    def __init__(self, ls_all, filterOption, price_from, price_to, isAcsending):
        self.__ls_all = ls_all
        self.__filterOption = filterOption
        self.__price_from = price_from
        self.__price_to = price_to
        self.__isAcsending = isAcsending
        

    def filterAndGetItems(self):
        
        ls_all = self.__ls_all[:]

        if self.__filterOption == None:
            self.__filterOption = "No"
        
        shippingFilter = ShippingFilter()

        if self.__filterOption.find('shipping') == -1 and self.__filterOption.find('No') == -1:
            
            # ls_all = filterPrices(ls_all, price_from, price_to)[:]
            priceGreaterThan = PriceGreaterThan(self.__price_from)
            priceLessThan = PriceLessThan(self.__price_to)
            andFilter = AndFilter(priceGreaterThan, priceLessThan)
            ls_all = andFilter.applyFilter(ls_all)[:]

        if self.__filterOption != None and self.__filterOption.find('No') == -1:
            # ls_all = filterBy(ls_all, filterOption, isAcsending)[:]
            shippingFilter = ShippingFilter()
            ls_all = shippingFilter.applyFilter(ls_all)[:]
            if self.__filterOption == "shipping":
                shippingFilter = ShippingFilter()
                ls_all = shippingFilter.applyFilter(ls_all)[:]

            elif self.__filterOption == "price":
                ls_all = sorted(ls_all, key = lambda row: float(row[1][:-1]))
                _ls_temp = []
                for elem in ls_all:
                    if elem[1] != "---":
                        _ls_temp.append(elem)  
                ls_all = _ls_temp[:]

            ls_all = self.__getSorted(ls_all)

        return ls_all


    def __getSorted(self, ls_all):
        ls_all__ = ls_all[:]
        if self.__isAcsending == "true":
            self.__isAcsending = True
        else:
            self.__isAcsending = False

        if self.__isAcsending != None and not self.__isAcsending:
            ls_all__ = ls_all__[::-1]
        return ls_all__
        


# def filterBy(ls_all__, filterOption, isAcsending):
# if filterOption == "shipping":
#     _nonShipable = []
#     _shipable = []
#     for elem in ls_all__:
#         if elem[1] == "---":
#             _nonShipable.append(elem)
#         else:
#             _shipable.append(elem)
#     ls_all__ = _nonShipable[:]
#     ls_all__.extend(_shipable)

# elif filterOption == "price":
#     ls_all__ = sorted(ls_all__, key = lambda row: row[1])
#     _ls_temp = []
#     for elem in ls_all__:
#         if elem[1] != "---":
#             _ls_temp.append(elem)  
#     ls_all__ = _ls_temp[:]

# if isAcsending == "true":
#     isAcsending = True
# else:
#     isAcsending = False

# if isAcsending != None and not isAcsending:
#     ls_all__ = ls_all__[::-1]
# return ls_all__

# def filterPrices(ls_all__, price_from, price_to):
#     if price_from == None:
#         price_from = 0
#     if price_to == None:
#         price_to = 100000000
    
#     _ls_temp = []
#     for elem in ls_all__:
#         if elem[1] != "---" and elem[1].find('price') == -1 and elem[1].find(",") == -1 and float(elem[1][:-1]) >= int(price_from) and float(elem[1][:-1]) <= int(price_to):
#             _ls_temp.append(elem)  
#     ls_all__ = _ls_temp[:]
#     return ls_all__