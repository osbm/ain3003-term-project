from flask import Flask, jsonify, request, render_template
from flask_pymongo import PyMongo

import os

# get mongo uri from env
mongo_uri = os.getenv("MONGO_URI")
print("mongo_uri: ", mongo_uri)

app = Flask(__name__, template_folder="templates")
app.config["MONGO_URI"] = mongo_uri + "/bookstoredatabase"

# database name is bookstoredatabase
# collection name is bookstorecollection

mongo = PyMongo(app)

@app.route("/books", methods=["GET"])
def get_all_books():
    books = mongo.db.bookstorecollection
    output = []
    for book in books.find():
        output.append(
            {
                "title": book["title"],
                "author": book["author"],
                "isbn": book["isbn"],
                "price": book["price"],
            }
        )
    return jsonify({"result": output})

@app.route("/books/add", methods=["GET"])
def render_add_book_form():
    return render_template("add_book.html")


@app.route("/")
def index():
    return render_template("index.html")

# add a book
@app.route("/books", methods=["POST"])
def add_book():
    books = mongo.db.bookstorecollection
    title = request.json["title"]
    author = request.json["author"]
    isbn = request.json["isbn"]
    price = request.json["price"]
    
    book_id = books.insert_one(
        {"title": title, "author": author, "isbn": isbn, "price": price}
    ).inserted_id
    
    new_book = books.find_one({"_id": book_id})
    output = {
        "title": new_book["title"],
        "author": new_book["author"],
        "isbn": new_book["isbn"],
        "price": new_book["price"],
    }
    return jsonify({"result": output})



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
