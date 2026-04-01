import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# soup.find(TAG, ATTRIBUTE)
title = soup.find("h1")
print("Title:",title.text)

price = soup.find("p", class_= "price_color")
print(f"Price: {price.text}")


# print(response)
# print(response.text)
# print(soup.prettify())
