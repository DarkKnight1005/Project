from .webscraper import *
from bs4 import BeautifulSoup
from selenium import webdriver
from pathlib import Path
import csv
import os
from src.models import *

class TapAzScraper(Scraper):
    def __init__(self, siteName, url, itemName, productLimit, driver):
        super().__init__(siteName, url, itemName, productLimit, driver);
    
    def doScrape(self):
        item = super().getItemName()
        ads_data = []
        url = f'https://tap.az/elanlar?utf8=%E2%9C%93&log=true&keywords={item}&q%5Bregion_id%5D='
        html = super()._get_html(url)
        soup = BeautifulSoup(html, 'lxml')

        cards = soup.find_all('div', class_='products-i rounded')
        for card in cards:
            data = self._scrape_data(card)
            shopItem = ShopItem(data["title"], data["price"], data["link"], data["site"])
            ads_data.append(shopItem)
        
        return ads_data

       

    def _scrape_data(self, card):
        link = card.find('a', class_='products-link').get('href')
        title = card.find('div', class_='products-top').img.get('alt')
        price = card.find('div', class_='products-price-container')

        if price is None:
            print('')
        else:
            Price = price.div.span.text

        link = self.getUrl() + link
        title += "(" + self.getName() + ")"

        data = {'title': title, 'price': Price, 'link': link, 'site': 'tapaz'}
        return data
  