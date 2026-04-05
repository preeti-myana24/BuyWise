from textblob import TextBlob #TextBlob is a class to analyse and understand text

#test text
'''
text = "This product is really amazing!"

#creating TextBlob object (converting normal text into object)
# this is a smart obj containing setiment, words, noun_phrases etc 
# these are built-in functions attached to the obj
analysis = TextBlob(text)

print(analysis.sentiment)

'''

#for scraping from the url 
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("h3")

first_title = books[0].find("a")["title"]

analysis = TextBlob(first_title)

print(first_title)
print(analysis.sentiment)