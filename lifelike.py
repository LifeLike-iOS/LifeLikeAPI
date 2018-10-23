#!/usr/bin/env python3

# import connexion
from flask import Flask
app = Flask(__name__)

import pymongo
url = "mongodb://_:%s@stitch.mongodb.com:27020/?authMechanism=PLAIN&authSource=%sexternal&ssl=true&appName=lifelike-biukf:mongodb-atlas:api-key" % ('pE1r3IXYjPGmySQ3fSOT8Fn9ishrFrj6nREzPnFXyy2pEKQvH3DYX5D3jTbgcOzL', '%24')
client = pymongo.MongoClient(url)
db = client.lifelike
collection = db.books

@app.route('/')
def hello_world():
    return 'Hello, World!'