#!/usr/bin/env python3
import pymongo
from bson import ObjectId
import datetime
import gridfs

url = "mongodb://_:%s@stitch.mongodb.com:27020/?authMechanism=PLAIN&authSource=%sexternal&ssl=true&appName=lifelike-biukf:mongodb-atlas:api-key" % ('pE1r3IXYjPGmySQ3fSOT8Fn9ishrFrj6nREzPnFXyy2pEKQvH3DYX5D3jTbgcOzL', '%24')
client = pymongo.MongoClient(url)

db = client.lifelike
fs = gridfs.GridFS(db)

collection = db.books
#collection.delete_one({"_id": ObjectId('5bce3bf3a9a32a4785dfff2c')})
imageFile = open('assets/coffeepot.jpg', 'r')
image = fs.put(imageFile)
# test_book = {
#                 "title": "The Design of Everyday Things",
#                 "authors": ["Donald A. Norman"],
#                 "ISBN_13": "9780465050659",
#                 "publisher": "Basic Books",
#                 "publication-date": datetime.datetime(2013, 11, 5),
#                 "page_count": 368,
#                 "chapter_count": 7,
#                 "chapters": [{
#                         "chapter_num": 1,
#                         "chapter_title": "The Psychopathology of Everyday Things",
#                         "page_count": 33,
#                         "pages": [
#                             {
#                                 "page_number": 2,
#                                 "image_count": 1,
#                                 "images": [
#                                     {
#                                         "image_title": "1.1 Carelman's Coffeepot for Masochists",
#                                         "image_file": image
#                                     }
#                                 ]
#                             }
#                         ]
#                     },
#                     {
#                         "chapter_num": 2,
#                         "chapter_title": "The Psychology of Everyday Actions",
#                         "page_count": 20
#                     }
#                 ]
#             }
# collection.insert_one(test_book)