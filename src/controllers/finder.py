from .formater import *
from src.Scrapers import *
from .filterService import *

class Finder:
    def __init__(self, itemToFind):
        self.itemToFind = itemToFind
    
    def makeSearch(self, store_list, currency):
        ls_all = []
        ls_amazon = []
        ls_tapaz = []

        if store_list == None:
            store_list = "";
        

        _store_list = store_list.lower().split("_")
        print(_store_list)

        amazonScraper = AmazonScraper("Amazon", "https://amazon.com", self.itemToFind, 20)
        tapAzScrapper = TapAzScraper("TapAz", "https://tap.az", self.itemToFind, 20)

        if "amazon" in _store_list:
            amazonScraper.doScrape();
        if "tapaz" in _store_list:
            tapAzScrapper.doScrape();
        
        formater = Formater()
        ls_all = formater.format(currency)

        return ls_all