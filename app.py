from flask import Flask, jsonify, request, render_template, redirect, url_for
from pymongo import MongoClient

import os

# prepare mongo connection
mongo_uri = os.getenv("MONGO_URI")
print("mongo_uri: ", mongo_uri)
mongo_client = MongoClient(mongo_uri + "/bookstoredatabase")
database = mongo_client["bookstoredatabase"]
collection = database["bookstorecollection"]

# prepare flask app
app = Flask(__name__, template_folder="templates")


# database name is bookstoredatabase
# collection name is bookstorecollection

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/books", methods=["GET"])
def get_all_books():
    books = collection.find()
    return render_template("show_books.html", books=books)

@app.route("/books/restore", methods=["GET"])
def restore_all_books():
    # drop collection
    collection.drop()
    # recreate collection from bookstrore.json
    
    # import documents from json file
    import json
    with open("bookstore.json") as f:
        books = json.load(f)
    collection.insert_many(books)

    books = collection.find()
    return render_template("show_books.html", books=books)

@app.route("/books/add", methods=["GET", "POST"])
def add_book_form():
    if request.method == "GET":
        return render_template("add_book.html")
    else:
        book = request.form
        collection.insert_one(
            {
                "isbn": book["isbn"],
                "title": book["title"],
                "author": {
                    "firstName": book["author_first_name"],
                    "lastName": book["author_last_name"]
                },
                "year": book["year"],
                "price": book["price"]
            }
        )
        return redirect(url_for("get_all_books"))

@app.route("/books/<book_isbn>", methods=["GET"])
def get_book(book_isbn):
    book = collection.find_one({"isbn": book_isbn})
    return render_template("show_book.html", book=book)


@app.route("/books/<book_isbn>/edit", methods=["GET", "POST"])
def edit_book(book_isbn):
    if request.method == "GET":
        book = collection.find_one({"isbn": book_isbn})
        return render_template("edit_book.html", book=book)
    else:
        book = request.form
        collection.update_one(
            {"isbn": book_isbn},
            {"$set":
                {
                    "isbn": book["isbn"],
                    "title": book["title"],
                    "author.firstName": book["author_first_name"],
                    "author.lastName": book["author_last_name"],
                    "year": book["year"],
                    "price": book["price"]
                }
            },
            upsert=True
        )
        return redirect(url_for("get_all_books"))

@app.route("/books/<book_isbn>/delete", methods=["GET"])
def delete_book(book_isbn):
    book = collection.find_one({"isbn": book_isbn})
    collection.delete_one({"isbn": book_isbn})
    return redirect(url_for("get_all_books"))


@app.route("/books", methods=["POST"])
def add_book():
    book = request.form
    collection.insert_one(book)
    return render_template("add_book.html", book=book)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
