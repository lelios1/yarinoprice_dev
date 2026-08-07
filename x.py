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
    print(f"{i + 1} out of {len(pages)}")

    tag = page.soup.find_all("div", class_="product-description") # Get info for name and price
    for y in range(0, len(tag), 3):
        product = tag[y].text.strip()
        eurosplit = product.split("€")
        name = product.split("|")[0].strip()
        price = eurosplit[1]
        try:    #Check if there is an original price to get else set to price
            original_price = eurosplit[2]
        except:
            original_price = price
        names.append(name)
        prices.append(price)
        original_prices.append(original_price)
        types.append(type_web[i])

    tag_img = page.soup.find_all("img", class_="tvproduct-defult-img tv-img-responsive") # Get image links
    for y in range(0, len(tag_img), 4):
        images.append(tag_img[y]["src"])

    tag_stock = page.soup.find_all("div", class_="tvproduct-image") # Check if it's in stock
    for y in range(0, len(tag_stock), 4):
            if "Out Of Stock" in tag_stock[y].text: stock.append(False)
            else: stock.append(True)

for i in range(0, len(names)):
    print(f"Name: {names[i]} \nPrice: {prices[i]} \nOriginal Price: {original_prices[i]} \nStock: {stock[i]} \nImage: {images[i]} \nType: {types[i]}", end = '\n\n')

print(len(names))

mode = 'a'

with open('data.csv', mode, encoding="utf-8", newline='') as csvfile:
    fieldnames = ['Name', 'Price', 'Original Price', 'Image', 'Type', 'Stock', 'Date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    if mode != 'a':
        writer.writeheader()
    for i in range(0, len(names)):
        writer.writerow({'Name': names[i], 'Price': prices[i], 'Original Price': original_prices[i], 'Image': images[i], 'Type': types[i], 'Stock': stock[i], 'Date': date.today()})