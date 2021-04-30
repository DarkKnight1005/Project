# from bs4 import BeautifulSoup
# from selenium import webdriver
# from pathlib import Path
# import csv
# import os

# browser = webdriver.Chrome(executable_path="/Users/ayazpanahov/Desktop/BHOS/OOP/Project/chromedriver")

# def write_csv(ads):
#     with open('results.csv', 'a+') as f:
#         fields = ['title', 'price', 'link', 'site']

#         writer = csv.DictWriter(f, fieldnames=fields)

#         for ad in ads:
#             writer.writerow(ad)


# def get_html(url):

#     browser.get(url)
#     return browser.page_source


# def scrape_data_amazon(card):
#     try:
#         h2 = card.h2

#     except:
#         title = ''
#         link = ''

#     else:
#         title = h2.text.strip()
#         link = h2.a.get('href')

#     try:
#         price = card.find(
#             'span', class_='a-price-whole').text.strip('.').strip()
#     except:
#         price = ''
#     else:
#         price = ''.join(price.split(','))

#     data = {'title': title, 'price': price, 'link': link, 'site': 'amazon'}
#     return data


# def scraperAmazon(item):
#     ads_data = []
#     _f = open("results.csv", "w+")
#     _f.write("_")
#     _f.close();
#     os.remove("results.csv")
#     _f = open("results.csv", "x")
#     _f.close();

#     for i in range(1, 5):
#         url = f'https://www.amazon.com/s?k={item}&page={i}&qid=1617285727&ref=sr_pg_2'
#         html = get_html(url)

#         soup = BeautifulSoup(html, 'lxml')

#         cards = soup.find_all(
#             'div', {'data-asin': True, 'data-component-type': 's-search-result'})

#         for card in cards:
#             data = scrape_data_amazon(card)
#             ads_data.append(data)

#     with open('results.csv', 'a+') as f:
#         f.write("title,price,link,site\n")
#     f.close()
#     write_csv(ads_data)


# def scraperTapAz(item):
#     ads_data = []
#     # _f = open("results.csv", "w+", encoding='utf-8')
#     # _f.write("")
#     # _f.close()
#     # os.remove("results.csv")
#     # _f = open("results.csv", "x", encoding='utf-8')
#     # _f.close()
#     url = f'https://tap.az/elanlar?utf8=%E2%9C%93&log=true&keywords={item}&q%5Bregion_id%5D='
#     html = get_html(url)
#     soup = BeautifulSoup(html, 'lxml')

#     cards = soup.find_all('div', class_='products-i rounded')
#     for card in cards:
#         data = scrape_dataTapAz(card)
#         ads_data.append(data)

#     with open('results.csv', 'a+', encoding='utf-8') as f:
#         f.write("title,price,link,site\n")
#     f.close()
#     write_csv(ads_data)

# def scrape_dataTapAz(card):

#     link = card.find('a', class_='products-link').get('href')
#     title = card.find('div', class_='products-top').img.get('alt')
#     price = card.find('div', class_='products-price-container')

#     if price is None:
#         print('')
#     else:
#         Price = price.div.span.text

#     Link = 'https://tap.az' + link
#     data = {'title': title, 'price': Price, 'link': Link, 'site': 'tapaz'}
#     return data

import abc


class Scraper(metaclass=abc.ABCMeta):
    def __init__(self, itemName, itemLimit):
        self.itemName = itemName
        self.itemLimit = itemLimit
    @abc.abstractmethod
    def _doScrape(self):
        pass

    def getItemLimit(self):
        return self.itemLimit
    
    def setItemLimit(self, newItemLimit):
        self.itemLimit = newItemLimit
        return self.itemLimit
    