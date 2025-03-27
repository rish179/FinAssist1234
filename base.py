from twitter_api import Stock_News
from sentiment_analyser import Sentiment_Analyser

class fin_assist:
    def chat_asssit(self, stock):
        tweetlist = Stock_News.fetch_yahoo_finance_news_today(self, stock_symbol=stock)
        sentiment = Sentiment_Analyser.analyse(self, tweetlist)
        print(sentiment)


if __name__ == "__main__":
    fn = fin_assist()
    fn.chat_asssit("AAPL")