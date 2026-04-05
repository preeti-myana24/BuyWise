# 🛒 BuyWise - Smart Product Analyzer

## 📌 Overview
BuyWise is a data-driven product analysis system that helps users decide whether to **Buy, Wait, or Avoid** a product based on sentiment analysis and pricing.

---

## 🚀 Features
- 🌐 Web scraping using BeautifulSoup
- 🧠 Sentiment analysis using TextBlob
- ⚖️ Decision logic (Buy / Wait / Avoid)
- 📊 Graph visualization using Matplotlib
- 🎨 Interactive UI using Streamlit
- 📁 CSV export of filtered results

---

## 🛠️ Tech Stack
- Python
- BeautifulSoup
- TextBlob
- Matplotlib
- Streamlit

---

## 📊 How It Works
1. Scrapes product data from a website
2. Analyzes product title sentiment
3. Combines sentiment + price logic
4. Classifies products:
   - ✅ Buy
   - ⏳ Wait
   - ❌ Avoid
5. Displays results in UI and graph

---

## ▶️ How to Run

### Install dependencies:
```bash
pip install requests beautifulsoup4 textblob matplotlib streamlit
