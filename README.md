# TRADESENSE

🚀 Introduction

Financial markets are highly influenced by news sentiment, and traders must process vast amounts of information in real time. Stock Sentiment Analyzer automates this process using Natural Language Processing (NLP) and AI-driven sentiment analysis to provide actionable trading insights.

This project integrates multiple APIs to fetch news, analyze sentiment, and predict stock actions based on real-time data.

⚙️ Technical Overview
🔹 System Architecture

## **Frontend**:

Accepts a CSV file containing the user's stock portfolio (list of ticker symbols). Shows related news personalised based on the users Portfolio.

Built using React.js,HTML/CSS to provide an intuitive UI.

## **Data Collection Layer**:

Fetches real-time stock-related news from multiple sources using APIs:

Twitter API – Extracts tweets mentioning the stock ticker.

Yahoo Finance API – Retrieves market news and financial reports.

Bing News API – Gathers news articles related to the stock.

Google News API – Sources trending financial articles.

Filters and preprocesses the data to remove duplicate or irrelevant content.

## **Sentiment Analysis & AI Processing**:

Aggregated news articles are sent to Azure GPT-4 API, where:

Sentiment analysis is performed (positive, negative, or neutral).

Contextual understanding helps in refining investment decisions.

Uses prompt engineering to tailor GPT-4 responses for stock sentiment evaluation.


## **Decision-Making Engine**:

Sentiment scores are mapped to trading decisions:

Positive sentiment → Buy recommendation 📈

Negative sentiment → Sell recommendation 📉

Neutral sentiment → Hold recommendation 🔍

Implements a rule-based approach to adjust predictions based on stock trends.

## **Backend & API Management**:

Developed using Python, Flask for efficient API handling.



## 🔹 Why This Approach?
✔ Real-Time Market Analysis – Automates financial news tracking.
✔ AI-Powered Sentiment Analysis – Uses GPT-4 for deep contextual understanding.
✔ Multi-Source Data Aggregation – Ensures a more holistic market view.
✔ Scalable Architecture – Can handle multiple users and large datasets.
✔ Customizable Decision Engine – Users can tweak decision parameters based on risk appetite.

🚀 Future Enhancements
Integrate Trading APIs (Zerodha, Alpaca, Interactive Brokers) for automated trades.

Enhance accuracy by combining GPT-4 with FinBERT sentiment analysis.

Use LLM fine-tuning for improved stock-specific sentiment predictions.
