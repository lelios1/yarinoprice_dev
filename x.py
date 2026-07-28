import mechanicalsoup

browser = mechanicalsoup.Browser()

page = browser.get("https://yarinohanzo.com/iaito-katana-accessories/katana-practical-iaito/")
tag = page.soup.select("#products")

products = []
products = str(tag[0].text).split("\n\n")

#for product in products:
#    print(product, end = '\n------------------------------------------------------------------\n')


func 
info = tag[0].find_all("img")

for i in range(0, len(info), 8):    #Get images for thumbnails
    if (info[i]['class'] == ['tvproduct-defult-img', 'tv-img-responsive']) : print(f"{info[i]['src']} \n ------------------- \n")