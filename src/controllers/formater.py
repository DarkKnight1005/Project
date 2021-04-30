import csv
from src.Helpers import *

class Formater:
    def __init__(self):
        pass

    def format(self, currency):

        ls_all = []
        mathHelper = MathHelper()

        with open('results.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    if row["price"] != "" and row["price"].find('price') == -1 and row["price"].find(",") == -1:
                        if currency == "azn":     
                            if row["site"] == "tapaz":
                                row["price"] = row["price"] + "₼" # ₼
                            else:
                                row["price"] = str(mathHelper.truncate(int(row["price"].replace(" ", "")) * 1.7, 2)) + "₼"
                        else: # us dollars
                            if row["site"] == "tapaz":
                                row["price"] = str(mathHelper.truncate(int(row["price"].replace(" ", "")) / 1.7, 2)) + "$"
                            else:
                                row["price"] = row["price"] + "$"
                    else:
                        row["price"] = "---"

                    ls_temp = [row["title"], row["price"], row["link"], row["site"]]
                    ls_all.append(ls_temp)
                line_count = line_count + 1

        return ls_all