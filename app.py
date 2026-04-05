import streamlit as st
import matplotlib.pyplot as plt
from scraper_clean import fetch_data,analyze_book

st.title("🛒 BuyWise - Smart Product Analyzer")
st.subheader("📊 Decision Results")
st.write("Analyze Products using sentiment + price intelligence")

books,prices = fetch_data()

buy = 0
wait = 0
avoid = 0
for i,(book,price) in enumerate(zip(books, prices),1):
        title = book.find("a")["title"]
        price_text = price.text.replace("Â","")
        price_value = float(price_text[1:]) 

        sentiment,decision = analyze_book(title,price_value)

        
        if decision == "Buy":
            buy += 1
            st.success(f"✅ {title} | {price_text}")
        elif decision == "Wait":
            wait += 1
            st.warning(f"⏳ {title} | {price_text}")
        else:
            avoid += 1
            st.error(f"❌ {title} | {price_text}")

st.write("### Summary")
st.write(f"✅ Buy: {buy} | ⏳ Wait: {wait} | ❌ Avoid: {avoid}")

#graph 
labels = ["Buy", "Wait", "Avoid"]
values = [buy, wait, avoid]

fig, ax = plt.subplots()
ax.bar(labels, values)
ax.set_title("Decision Analysis")

st.pyplot(fig)