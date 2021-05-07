import csv
from src.Helpers import *
from src.models import *

class Formater:
    def __init__(self):
        pass

    def format(self, currency, elements):

        ls_all = []
        mathHelper = MathHelper()

        # with open('results.csv', mode='r') as csv_file:
        #     csv_reader = csv.DictReader(csv_file)
        #     line_count = 0
        #     for row in csv_reader:
        #         if line_count != 0:
        #             if element.price != "" and element.price.find('price') == -1 and element.price.find(",") == -1:
                    #     if currency == "azn":     
                    #         if row["site"] == "tapaz":
                    #             element.price = element.price + "₼" # ₼
                    #         else:
                    #             element.price = str(mathHelper.truncate(int(element.price.replace(" ", "")) * 1.7, 2)) + "₼"
                    #     else: # us dollars
                    #         if row["site"] == "tapaz":
                    #             element.price = str(mathHelper.truncate(int(element.price.replace(" ", "")) / 1.7, 2)) + "$"
                    #         else:
                    #             element.price = element.price + "$"
                    # else:
                    #     element.price = "---"

        #             ls_temp = [row["title"], element.price, row["link"], row["site"]]
        #             ls_all.append(ls_temp)
        #         line_count = line_count + 1

        for element in elements:
            if element.price != "" and element.price.find('price') == -1 and element.price.find(",") == -1:
                if currency == "azn":     
                    if element.site == "tapaz":
                        element.price = element.price + "₼" # ₼
                    else:
                        element.price = str(mathHelper.truncate(int(element.price.replace(" ", "")) * 1.7, 2)) + "₼"
                else: # us dollars
                    if element.shopName == "tapaz":
                        element.price = str(mathHelper.truncate(int(element.price.replace(" ", "")) / 1.7, 2)) + "$"
                    else:
                        element.price = element.price + "$"
            else:
                element.price = "---"

        ls_all = elements[:]

        return ls_all