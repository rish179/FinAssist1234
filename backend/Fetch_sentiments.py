from flask_restful import Resource
from flask import request
import time
import sentiment_analyser 

class Fetch_sentiments(Resource):
    def post(self):
        rec_data = request.json # {'news':,"symbol":}

        # print(rec_data)

        sentiment_temp = sentiment_analyser.analyse( [content['summary'] for content in rec_data['news']])

        if sentiment_temp.isnumeric():
            print(sentiment_temp , " WAITING ")
            time.sleep(int(sentiment_temp))
            sentiment_temp = sentiment_analyser.analyse( [content['summary'] for content in rec_data['news']])

            if sentiment_temp.isnumeric():
                sentiment_temp = ""

        return {
            'Symbol':rec_data['symbol'],
            'Sentiments':sentiment_temp
        }