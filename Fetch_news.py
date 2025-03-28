from bs4 import BeautifulSoup
import requests
import tweepy
from datetime import datetime, timezone


def fetch_yahoo_finance_news_today(stock_symbol, count=5):
    url = f"https://finance.yahoo.com/quote/{stock_symbol}/news"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"[Yahoo] Failed to fetch for {stock_symbol}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    article_sections = soup.find_all('section', {'data-testid': 'storyitem'})

    news_list = []
    for section in article_sections:
        try:
            # Timestamp text (e.g. "Yahoo Finance Video • 1 hour ago")
            footer = section.find('div', class_='publishing')
            timestamp = footer.text.strip() if footer else ''
            if not any(keyword in timestamp.lower() for keyword in ["hour ago", "hours ago", "minute ago", "minutes ago", "today"]):
                continue  # Skip anything not posted today

            # Headline
            h3 = section.find('h3')
            headline = h3.text.strip() if h3 else None

            # Link
            a_tag = section.find('a', href=True)
            link = 'https://finance.yahoo.com' + a_tag['href'] if a_tag and a_tag['href'].startswith('/') else a_tag['href']

            # Summary
            summary_tag = section.find('p')
            summary = summary_tag.text.strip() if summary_tag else ''

            news_list.append({
                'headline': headline,
                'url': link,
                'summary': summary,
                'source': 'Yahoo Finance',
                'timestamp': timestamp
            })

            if len(news_list) >= count:
                break  # Stop after getting desired number of today's news

        except Exception as e:
            print("Error parsing section:", e)

    return news_list

def fetch_twitter_news_today(stock_symbol, twitter_bearer_token, count=10):
    twitter_bearer_token = "AAAAAAAAAAAAAAAAAAAAAJIZ0AEAAAAAiaN8dDcs%2FS5%2F1rZ5X5mabrSXQhU%3D57C7pIC39JgoIsYtVt43GKMwI7uPOuvyVaKLpuK4EzXFGBfeh9"
    client = tweepy.Client(bearer_token=twitter_bearer_token)

    query = f"{stock_symbol} -is:retweet lang:en"
    tweets = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at'])

    tweet_list = []
    now = datetime.now(timezone.utc)
    
    if tweets.data:
        for tweet in tweets.data:
            created_at = tweet.created_at  # already in UTC datetime
            # Check if the tweet is from today (last 24 hours)
            time_diff = now - created_at
            if time_diff.total_seconds() > 86400:
                continue  # skip older than 1 day

            tweet_list.append({
                'headline': tweet.text,
                'url': f"https://twitter.com/i/web/status/{tweet.id}",
                'source': 'Twitter',
                'timestamp': created_at.isoformat()
            })

            if len(tweet_list) >= count:
                break
    else:
        print(f"[Twitter] No tweets found for {stock_symbol}")
    
    return tweet_list

def fetch_news_api_today(stock_symbol, count=5):
    API_KEY = "9753258da1534e529200ad6a76e1f034"
    url = f"https://newsapi.org/v2/everything?q={stock_symbol}&sortBy=publishedAt&language=en&apiKey={API_KEY}"

    response = requests.get(url)
    news_data = response.json()
    news_list=[]
    if news_data["status"] == "ok":
        articles = news_data["articles"][:count]  # Get top 5 news articles
        for article in articles:
            news_list.append({
            'headline': article['title'],
            'url': article['url'],
            'summary': article['content'],
            'source':  article['source']['name'],
            'timestamp':  article['publishedAt']
            })
    else:
        print("Error fetching news")
    return news_list