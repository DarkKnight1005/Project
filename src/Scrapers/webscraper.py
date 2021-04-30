from bs4 import BeautifulSoup
from selenium import webdriver
from pathlib import Path
from src.Website import * 
import csv
import os
import abc

browser = webdriver.Chrome(executable_path="/Users/ayazpanahov/Desktop/BHOS/OOP/Project/chromedriver")

class Scraper(Website, metaclass=abc.ABCMeta):

    def __init__(self, siteName, url, itemName, itemLimit):
        super().__init__(siteName, url);
        self.__itemName = itemName
        self.__itemLimit = itemLimit

    @abc.abstractmethod
    def doScrape(self):
        pass

    @abc.abstractmethod
    def _scrape_data(self, card):
        pass

    def _writeCsv(self, ads):
        with open('results.csv', 'a+') as f:
            fields = ['title', 'price', 'link', 'site']

            writer = csv.DictWriter(f, fieldnames=fields)

            for ad in ads:
                writer.writerow(ad)

    def _get_html(self, url):
        browser.get(url)
        return browser.page_source

    def getItemLimit(self):
        return self.__itemLimit
    
    def setItemLimit(self, newItemLimit):
        self.itemLimit = newItemLimit
        return self.__itemLimit

    def getItemName(self):
        return self.__itemName
