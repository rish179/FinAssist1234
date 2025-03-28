from flask_restful import Resource
from flask import request
import pandas as pd
import sentiment_analyser 
import Fetch_news

import time

class Upload_csv(Resource):
    def post(self):
        # Check if a file is part of the request

        if 'file' not in request.files:
            print(f"Admin <> Upload csv <> error : No file part in the request")

        file = request.files['file']

        # Check if a file was selected
        if file.filename == '':
            print(f"Admin <> Upload csv <> error : No selected file")

        # Check the file type
        if not file.filename.endswith('.csv'):
            print(f"Admin <> Upload csv <> error : Invalid file type. Only CSV files are allowed.")

        try:
            # Read the CSV file into a pandas DataFrame
            df_holdings = pd.read_csv(file)

            print(df_holdings)

            news = []

            # sentiment = []

            for stk_symb in df_holdings['Stocks'].unique().tolist():
                # yh_news_ = Stock_News.fetch_yahoo_finance_news_today(stk_symb)
                API_news = Fetch_news.fetch_news_api_today(stk_symb)

                # print(yh_news_ ,API_news)

                news.append([stk_symb,API_news])


                # sentiment_temp = sentiment_analyser.analyse( [content['summary'] for content in API_news[:1]])
                # time.sleep(4)

                # if sentiment_temp != '':
                #     time.sleep(10)
                #     sentiment_temp = sentiment_analyser.analyse( [content['summary'] for content in API_news[:1]])

                # sentiment.append([stk_symb,sentiment_temp])


            # print(sentiment)

            return {
                "Status": 'success',
                "message": "File Uploaded Successfully",
                'Holdings':df_holdings.to_json(orient='records'),
                'RelatedArticles':news}

        except Exception as e:
            print(f"Admin <> Upload csv <> Reason => {e}")
            return {"Status": 'error',"message": "Error occurred while uploading file",'Holdings':'{}','RelatedArticles':'{}'}