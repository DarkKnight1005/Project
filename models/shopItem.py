class ShopItem:
    def __init__(self, _name, _cost, _url):
        self.name = _name
        self.cost = _cost
        self.url = _url
    
    def getName(self):
        return self.name
    
    def getCost(self):
        return 