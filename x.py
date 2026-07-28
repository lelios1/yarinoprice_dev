from datetime import date

import mechanicalsoup
import csv

browser = mechanicalsoup.Browser()

type_web = ("basic", "practical", "special", "performance", "damascus", "superior")

pages = []

for type in type_web:
    pages.append(browser.get(f"https://yarinohanzo.com/iaito-katana-accessories/katana-{type}-iaito/"))

names = []
prices = []
original_prices = []
images = []
types = []
stock = []

for i, page in enumerate(pages):
    print(f"{i} out of {len(pages)}")
    tag = page.soup.select("#products")

    products = []
    products = str(tag[0].text).split("\n\n")

    for product in products:
        eurosplit = product.split("€")
        if len(eurosplit) < 2: continue
        x = product.split("\n")
        if "Out Of Stock" in x[0]: stock.append(False)
        else: stock.append(True)
        name = x[0].split(" | ")[0].replace(" Add To Cart ", "").replace("On sale!","").replace(" Out Of Stock","").replace("+","").replace("- ","")
        price = eurosplit[1]
        original_price = eurosplit[2].split("\n")[0]
        names.append(name)
        prices.append(price)
        original_prices.append(original_price)
        types.append(type_web[i])

    info = tag[0].find_all("img")
    for i in range(0, len(info), 8):    #Get images for thumbnails
        if (info[i]['class'] == ['tvproduct-defult-img', 'tv-img-responsive']) : images.append(info[i]['src'])

for i in range(0, len(names)):
    print(f"Name: {names[i]} \nPrice: {prices[i]} \nOriginal Price: {original_prices[i]} \nImage: {images[i]} \nType: {types[i]} \nStock: {stock[i]}", end = '\n\n')

mode = 'a'

with open('data.csv', mode, newline='') as csvfile:
    fieldnames = ['Name', 'Price', 'Original Price', 'Image', 'Type', 'Stock', 'Date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    if mode != 'a':
        writer.writeheader()
    for i in range(0, len(names)):
        writer.writerow({'Name': names[i], 'Price': prices[i], 'Original Price': original_prices[i], 'Image': images[i], 'Type': types[i], 'Stock': stock[i], 'Date': date.today()})