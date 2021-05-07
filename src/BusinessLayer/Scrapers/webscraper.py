from bs4 import BeautifulSoup
from selenium import webdriver
from pathlib import Path
from src.Website import * 
import csv
import os
import abc

class Scraper(Website, metaclass=abc.ABCMeta):

    def __init__(self, siteName, url, itemName, itemLimit, driver):
        super().__init__(siteName, url);
        self.__itemName = itemName
        self.__itemLimit = itemLimit
        self.__driver = driver

    @abc.abstractmethod
    def doScrape(self):
        pass

    @abc.abstractmethod
    def _scrape_data(self, card):
        pass

    def _get_html(self, url):
        self.__driver.getBrowser().get(url)
        return self.__driver.getBrowser().page_source

    def getItemLimit(self):
        return self.__itemLimit
    
    def setItemLimit(self, newItemLimit):
        self.itemLimit = newItemLimit
        return self.__itemLimit

    def getItemName(self):
        return self.__itemName
