# Mega Scrape

Webscraper which is used to searcha dn scrape data with some optional filters from Amazon and TapAz

## For Clients


### Usage
Usage of this web app is very simple. In search box write the name of desired product, then select some available ашдеукштп features and press the search button. Then after some magic occured you will see the scraped results.

### Features
Below you can see all available filtering fatures of this Webscraper.

- Search in Amazon or not
- Search in TapAz or not
- Currency:
  - AZN
  - USD
- Filter by:
  - Price
  - Available Shipping
- Order:
  - Ascending
  - Descending



## For Developers

### Initial Set Up
In order to deploy the project you will need python 3.9+ and pip installed. Running:
```
pip3 install -r requirements.txt
```
Now your environment is ready to run the project

### Deploy
By Simply navigating into project folder and executing the following command, the standalone version of the app will run:
```
python3 ./app.py
```
After this the standart syte version is running on the port which is specifed in the terminal (By default: 5000)

### Scraper Features
The scraper class have several features like:
- Custom Max Scraped Products Limit (by default 20)
- Custom Scraping Driver ([See Webdriver Part](###Webdriver))

### Webdriver
As developer you can choose which webdriver you would prefer to use, it can be chormium driver or firefox, does not matter. However, consider that project is using selenium webdriver, all webdrivers which is supported by selenium are also supported by Mega Scrape.
In order to change the webdriver,
1. Download new driver
2. Coopy the path
3. Create new Driver Object inside the app.py
4. When initializing the driver spesify exact path to the webdriver and its name(unique name is more desirable)
5. Pass it as argument into the "Finder"

It is also possible to have 2 separate webdrives by just creating and passing them.

### Site Template
In order to change site template locata into the `./templates/public/` folder and reaplce the markdown of base.html.

#### Note
Note: The name of main markdown have to be base.html.
Note: Site will take 2 arguments
1. Scraped results from Amazon
2. Scraped results from TapAz

Scraped results represented as list of ShopItem which is the model with the following parametrs:
- name (aka title)
- price
- url (to the page of product)
- shopName (name of the syte from which the product was scraped)

### Filter Extension
In order to create extension for the filters the new class inherited from the Filter class have to be created. Then `applyFilter` method have to be overwriten and the modifed output should be presened.
After that new Filter extension is created and can be used in app and in "and" and "or"(can be implmeneted in case of necessity) filters.

### Other Extensions
The project has Model-View-Controller schema, so you can easyly add some new controllers or models into approptiate place and import them with `__init__.py` files. Some new folders can also be created, but then thet have to be added to the main init file which is located directly inside the `src` folder.

## Troubleshooting

For now troubleshooting is not supported in this documentation. If there are any questions please do not hesitate to contact with me via
```
Email: ayaz.panahov.std@bhos.edu.az
WhatsApp: +994507935935
```
--------------------------------------------------------------------
Made by Ayaz Panahov.
Copyright (c) 2021 HyandrDos Inc. All rights reserved.
