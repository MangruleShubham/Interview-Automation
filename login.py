from flask import Flask, render_template, request
from flask_login import LoginManager, login_user, logout_user, current_user
from connection import db

import os

from pymongo import MongoClient

# # Get the MongoDB connection string from the environment
# MONGODB_CONNECTION_STRING = os.environ["MONGODB_CONNECTION_STRING"]

# # Create a MongoClient object
# client = MongoClient(MONGODB_CONNECTION_STRING)

# # Get the database
# db = client.get_database("my_database")

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

@app.route("/")
def home():
    if current_user.is_authenticated:
        return render_template("home.html")
    else:
        return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    user = db.users.find_one({"username": username})

    if user is None or not user["password"] == password:
        return render_template("login.html", error="Invalid username or password")

    login_user(user)
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

@login_manager.user_loader
def load_user(user_id):
    return db.users.find_one({"_id": user_id})

class User(db.Document):
    username = db.StringField(unique=True)
    password = db.StringField()

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, password):
        return self.password == password

if __name__ == "__main__":
    app.run(debug=True)
