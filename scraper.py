import requests
import csv
from bs4 import BeautifulSoup
from textblob import TextBlob

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
prices = soup.find_all("p", class_ = "price_color")


'''
print(len(books))
print(books[0])
print(len(prices)) 
print(prices[0])
# print(books[0].text) - but this will only display the visible text 
print(books[0].find("a")["title"])
'''

# #creating an empty list and storing all the 20 titles
# titles=[]

# for book in books:
#     title = book.find("a")["title"]
#     print(title)

#sentiment contains subjectivity and polarity

#Create file,Write (overwrite), Write clean rows (no extra gaps), Support all characters safely
file = open("buywise_result.csv", "w", newline="",encoding="utf-8")
writer = csv.writer(file) # used to write structured data row by row into a CSV file

writer.writerow(["Index", "Title", "Price", "Sentiment", "Decision"])
for i,(book,price) in enumerate(zip(books, prices),1):
    title = book.find("a")["title"]
    price_text = price.text.replace("Â","")
    price_value = float(price_text[1:]) #to remove the unwanted symbol

    analysis = TextBlob(title)
    polarity = analysis.sentiment.polarity # we are also concerned with polarity rn

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    if sentiment == "Positive":
        if price_value < 30:
            decision = "Buy"
            writer.writerow([i,title,price_text,sentiment,decision])

        else:
            decision = "Wait"

    elif sentiment == "Negative":
        decision = "Avoid"
    else:
        # sentiment == "Neutral"
        decision = "Wait"

    if decision == "Buy":
        print(f"BUY: {title} | {price_text}")
    # print(f"{i}. {title} | {price_text} -> {sentiment} -> {decision}")
#we used price_text here to show the symbol also , but for comparing we convert it into
# price_value

file.close()
print("\nBuyWise: Filtered results saved successfully!")


# for t in titles: (skipping list)
#     print(t)

# print(response)
# print(response.text)
# print(soup.prettify())