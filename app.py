# LIBRARIES
from flask import Flask, request
from bson import json_util, ObjectId
import pymongo
import json
from flasgger import Swagger

# APP SET UP
app = Flask(__name__)
app.config['SWAGGER'] = {
    'title': 'Lifelike Books API',
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "model_filter": lambda tag: True,  # all in
        }
    ]
}
swagger = Swagger(app)
# app = connexion.FlaskApp(__name__, specification_dir='./')
url = "mongodb://_:%s@stitch.mongodb.com:27020/?authMechanism=PLAIN&authSource=%sexternal&ssl=true&appName=lifelike-biukf:mongodb-atlas:api-key" % ('pE1r3IXYjPGmySQ3fSOT8Fn9ishrFrj6nREzPnFXyy2pEKQvH3DYX5D3jTbgcOzL', '%24')
client = pymongo.MongoClient(url)
db = client.lifelike
collection = db.books

# ROUTES
@app.route('/')
def health_check():
    """
    file: ./docs/health_check.yml
    """
    return 'Heathly!', 200

# List all books
@app.route('/books', methods=['GET'])
def get_all_books():
    """
    file: ./docs/get_all_books.yml
    """
    try:
        books = collection.find()
        return json_util.dumps(books), 200
    except Exception as e:
        return error_message("Failed to retreieve data!")

# Text search for a book
@app.route('/books/search/<string:search_param>', methods=["GET"])
def search_for_book(search_param):
    """
    file: ./docs/search_for_book.yml
    """
    try: 
        results = search_by_keys(search_param)
        return json_util.dumps(results), 200
    except Exception as e:
        return error_message("Search failed!")

# Retrieve a book
@app.route('/books/<string:id>', methods=['GET'])
def get_book(id):
    """
    file: ./docs/get_book.yml
    """
    try:
        book = collection.find_one({"_id": ObjectId(id)})
        return json_util.dumps(book), 200
    except Exception as e:
        return error_message("Failed to retrieve book with id of " + id)

# Add book
@app.route('/books/add', methods=['POST'])
def add_book():
    """
    file: ./docs/add_book.yml
    """
    try:
        book_data = request.json
        collection.insert_one(book_data)
        return json.dumps({'success': True, 'message': book_data['title'] + ' added!'}), 200
    except Exception as e:
        return error_message("Failed to add book!")

# Edit book 
@app.route('/books/<string:id>/edit', methods=['PUT'])
def edit_book(id):
    """
    file: ./docs/edit_book.yml
    """
    try:
        updated_content = request.json
        book = collection.update({"_id": ObjectId(id)},{"$set": updated_content})
        edited_book = collection.find_one({"_id": ObjectId(id)})
        return json.dumps({'success': True, 'message': edited_book['title'] + ' updated!'}), 200
    except Exception as e:
        return error_message("Failed to update book with id of " + id)

# Delete book
@app.route('/books/<string:id>/delete', methods=['DELETE'])
def delete_book(id):
    """
    file: ./docs/delete_book.yml
    """
    try:
        deleted_book = collection.find_one({"_id": ObjectId(id)})
        collection.delete_one({"_id": ObjectId(id)})
        return json.dumps({'success': True, 'message': deleted_book['title'] + ' deleted!'}), 200
    except Exception as e:
        return error_message("Failed to delete book with id of " + id)

# ADDITIONAL METHODS

# Search function because pymongo indexing is failing
def search_by_keys(search_param):
    books = collection.find()
    results = []
    for book in books:
        print(book['title'])
        print(search_param in book['title'])
        if search_param in book['title'] or search_param in book['authors']:
            results.append(book)
        elif 'ISBN_13' in book and search_param == book['ISBN_13']:
            results.append(book)
    return results

def error_message(message):
    return json.dumps({'success': False, 'message': message}), 400

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    # app.run()