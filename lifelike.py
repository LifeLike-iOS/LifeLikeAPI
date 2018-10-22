#!/usr/bin/env python3

# import connexion
from flask import Flask
import pymongo
import urllib 
app = Flask(__name__)

username = urllib.parse.quote_plus('tiffanychen@cmu.edu')
password = urllib.parse.quote_plus('benjin!56fan')
client = pymongo.MongoClient("mongodb+srv://%s:%s@lifelike-cluster-rialo.mongodb.net/test?retryWrites=true"  % (username, password))
db = client.test

@app.route('/')
def hello_world():
    return 'Hello, World!'

# if __name__ == '__main__':
#     app = connexion.FlaskApp(__name__, specification_dir='./')
#     # app = Flask(__name__)
#     app.add_api('swagger.yaml', arguments={'title': 'Hello World Example'})
#     app.run()