from flask import Flask, redirect, url_for, render_template , request
# from webscraper import scraperAmazon, scraperTapAz
from src import *
import csv
import math
import os

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

mathHelper = MathHelper()

@app.route("/", methods=['GET', 'POST'])
def home():
    mf = MyForm()
    return render_template("./public/base.html", isSearching = False, form=mf)

@app.route("/find/<itemToFind>/stores/<store_list>/filterBy/<filterOption>/<isAcsending>/priceRange/from/<price_from>/to/<price_to>/currency/<currency>", methods=['GET', 'POST'])
def findPage(itemToFind, store_list = None, filterOption = None, isAcsending = None, price_from = None, price_to = None, currency = None):
    ls_amazon = []
    ls_tapaz = []
    ls_all = []
    if price_from == "NAN":
        price_from = None
    if price_to == "NAN":
        price_to = None
    finder = Finder(itemToFind)
    ls_all = finder.makeSearch(store_list, currency)[:]
    filterService = FilterService(ls_all, filterOption, price_from, price_to, isAcsending)
    ls_all = filterService.filterAndGetItems()[:]
    # print(ls_all)
    resultHandler = ResultHandler(ls_all)
    ls_amazon, ls_tapaz = resultHandler.handle()

    mf = MyForm()
    return render_template("./public/base.html", isSearching = True, itemsAmazon = ls_amazon, itemsTapAz = ls_tapaz, form = mf)


@app.route("/process", methods=['GET', 'POST'])
def process():
    pr = Process()
    pr.process()
    if request.method == "POST":
        # if request.form['submit_button'] == 'Search':
        storeList = ""
        currency = ""
        _filter = ""
        try:
            tmp = request.form["amazon"]
            if tmp == "on":
                storeList += "amazon_"
        except:
            pass
        
        try:
            tmp = request.form["tapaz"]
            if tmp == "on":
                storeList += "tapaz"
        except:
            pass

        try:
            currency = request.form["currency"]
            
        except:
            currency = "AZN"

        if storeList == "":
            return redirect(url_for("home"))

        _filter = request.form["Filter"].lower()
        isAscening = "true" if request.form["Order"].lower() != "Ascending" else "false"
        
        priceFrom = "NAN"
        priceTo = "NAN"
        if _filter == "price":
            try:
                priceFrom = request.form["priceFrom"]
            except:
                priceFrom = None

            try:
                priceTo = request.form["priceTo"]
            except:
                priceTo = None

        print(request.form)
        return redirect(url_for("findPage", itemToFind = request.form["itemToFind"], store_list = storeList, filterOption = _filter, isAcsending = isAscening, price_from = priceFrom, price_to = priceTo, currency = currency))
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
