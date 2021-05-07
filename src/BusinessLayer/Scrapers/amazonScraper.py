from .webscraper import *
from bs4 import BeautifulSoup
from selenium import webdriver
from pathlib import Path
import csv
import os
from src.models import *

class AmazonScraper(Scraper):
    def __init__(self, siteName, url, itemName, productLimit, driver):
        super().__init__(siteName, url, itemName, productLimit, driver);
    
    def doScrape(self):
        item = super().getItemName()
        ads_data = []

        for i in range(1, 5):
            url = f'https://www.amazon.com/s?k={item}&page={i}&qid=1617285727&ref=sr_pg_2'
            html = super()._get_html(url)

            soup = BeautifulSoup(html, 'lxml')

            cards = soup.find_all(
                'div', {'data-asin': True, 'data-component-type': 's-search-result'})

            for card in cards:
                data = self._scrape_data(card)
                shopItem = ShopItem(data["title"], data["price"], data["link"], data["site"])
                ads_data.append(shopItem)

        return ads_data

    def _scrape_data(self, card):
        try:
            h2 = card.h2

        except:
            title = ''
            link = ''

        else:
            title = h2.text.strip()
            link = h2.a.get('href')

        try:
            price = card.find(
                'span', class_='a-price-whole').text.strip('.').strip()
        except:
            price = ''
        else:
            price = ''.join(price.split(','))

        link = self.getUrl() + link
        title += "(" + self.getName() + ")"

        data = {'title': title, 'price': price, 'link': link, 'site': 'amazon'}
        return data
  