class ShopItem:
    def __init__(self, _name, _price, _url, shopName):
        self.name = _name
        self.price = _price
        self.url = _url
        self.shopName = shopName
    
    def getName(self):
        return self.name
    
    def getprice(self):
        return self.price

    def getUrl(self):
        return self.url

    def getShopName(self):
        return self.shopName

    def setprice(self, newprice):
        self.price = newprice
        return self.price