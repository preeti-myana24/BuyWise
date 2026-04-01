import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

# soup.find(TAG, ATTRIBUTE)
''' 
title = soup.find("h1")
# print("Title:",title.text)

# price = soup.find("p", class_= "price_color")
# print(f"Price: {price.text}")
'''

books = soup.find_all("h3")

'''
print(len(books))
print(books[0])
# print(books[0].text) - but this will only display the visible text 
print(books[0].find("a")["title"])
'''

# #creating an empty list and storing all the 20 titles
# titles=[]

# for book in books:
#     title = book.find("a")["title"]
#     print(title)

for i,book in enumerate(books,1):
    title = book.find("a")["title"]
    print(f"{i}. {title}")


# for t in titles: (skipping list)
#     print(t)



# print(response)
# print(response.text)
# print(soup.prettify())
