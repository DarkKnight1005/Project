from .formater import *
from src.BusinessLayer.Scrapers import *
from .filterService import *
from src.models import *

class Finder:
    def __init__(self, itemToFind, driver):
        self.itemToFind = itemToFind
        self.__driver = driver
    
    def makeSearch(self, store_list, currency):
        ls_all = []
        ls_amazon = []
        ls_tapaz = []

        if store_list == None:
            store_list = "";
        

        _store_list = store_list.lower().split("_")
        print(_store_list)

        amazonScraper = AmazonScraper("Amazon", "https://amazon.com", self.itemToFind, 20, self.__driver)
        tapAzScrapper = TapAzScraper("TapAz", "https://tap.az", self.itemToFind, 20, self.__driver)

        if "amazon" in _store_list:
            ls_amazon = amazonScraper.doScrape()[:];
            
        if "tapaz" in _store_list:
            ls_tapaz = tapAzScrapper.doScrape()[:];
        
        formater = Formater()

        ls_all = ls_amazon + ls_tapaz

        ls_all = formater.format(currency, ls_all)[:]

        return ls_all