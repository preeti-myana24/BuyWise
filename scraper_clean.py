import requests
import csv
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from textblob import TextBlob

def fetch_data():
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("h3")
    prices = soup.find_all("p", class_ = "price_color")
    return books,prices
    
def analyze_book(title,price_value):
    analysis = TextBlob(title)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    if sentiment == "Positive":
        if price_value < 30:
            decision = "Buy"
        else:
            decision = "Wait"

    elif sentiment == "Negative":
        decision = "Avoid"
    else:
        # sentiment == "Neutral"
        decision = "Wait"
    
    return sentiment,decision

def save_to_csv(i,title, price_text, sentiment, decision,writer):
    if decision in ["Buy", "Wait"]:
        writer.writerow([i,title,price_text,sentiment,decision])



def main():
    books,prices = fetch_data()
    
    buy_count = 0
    wait_count = 0
    avoid_count = 0

    file = open("buywise_result.csv", "w", newline="",encoding="utf-8")
    writer = csv.writer(file)

    writer.writerow(["Index", "Title", "Price", "Sentiment", "Decision"])

    for i,(book,price) in enumerate(zip(books, prices),1):
        title = book.find("a")["title"]
        price_text = price.text.replace("Â","")
        price_value = float(price_text[1:]) 

        sentiment,decision = analyze_book(title,price_value)

        if decision == "Buy":
            buy_count += 1
        elif decision == "Wait":
            wait_count += 1
        else:
            avoid_count += 1

        save_to_csv(i, title, price_text, sentiment, decision,writer)

        if decision == "Buy":
            print(f"BUY: {title} | {price_text}")


    labels = ["Buy","Wait","Avoid"]
    values = [buy_count,wait_count,avoid_count]

    plt.figure()
    plt.bar(labels, values)
    plt.title("BuyWise Decision Analysis")
    plt.xlabel("Decision Type")
    plt.ylabel("Number of Products")
    plt.show()

    file.close()

    print("\nBuyWise: Filtered results saved successfully!")

if __name__ == "__main__":
    main()