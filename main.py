from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS  # Comment this on deployment
import logging
from logging.handlers import RotatingFileHandler

# Import resources
from backend.Upload_csv import Upload_csv
from backend.Get_holdings import Get_holdings
from backend.Fetch_sentiments import Fetch_sentiments


app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app)  # Comment this on deployment
api = Api(app)


# # Set up RotatingFileHandler
# handler = RotatingFileHandler(r'C:\Users\samyak.jain\CLR Logs\CLR console.log', maxBytes=20000, backupCount=3)
# handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s %(levelname)s:: %(message)s')
# handler.setFormatter(formatter)
# app.logger.addHandler(handler)
# app.logger.setLevel(logging.DEBUG)


@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')

api.add_resource(Upload_csv, '/backend/upload_csv')
api.add_resource(Get_holdings, '/backend/Get_holdings')
api.add_resource(Fetch_sentiments, '/backend/Fetch_sentiments')

if __name__ == '__main__':
    app.run()
