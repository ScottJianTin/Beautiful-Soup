from bs4 import BeautifulSoup
import requests

url = "https://scrapingclub.com/exercise/list_basic/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
count = 1
products = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
for product in products:
    itemName = product.find("h4", class_="card-title").text.strip()
    itemPrice = product.find("h5").text
    print(f"{count}) Item Price: {itemPrice:>7}, Item Name: {itemName}")
    count += 1

pages = soup.find_all("a", class_="page-link")
links = []
for page in pages:
    pageNum = int(page.text) if page.text.isdigit() else None
    if pageNum != None:
        x = page.get("href")
        links.append(x)
# print(links)

for link in links:
    newUrl = url + link
    response = requests.get(newUrl)
    soup = BeautifulSoup(response.text, "lxml")
    products = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
    for product in products:
        itemName = product.find("h4", class_="card-title").text.strip()
        itemPrice = product.find("h5").text
        print(f"{count}) Item Price: {itemPrice:>6}, Item Name: {itemName}")
        count += 1

