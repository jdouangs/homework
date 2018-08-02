from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars


app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

collection = mydb["mars"]

@app.route("/")
def home():

    data = collection.find_one()

    return render_template("index.html", data=data)

@app.route("/scrape")
def scrape():

    update_data = scrape_mars.scrape()

    collection.insert_one(update_data)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)