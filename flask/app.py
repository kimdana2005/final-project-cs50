import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///plantings.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database

        message = ""
        name = request.form.get("name")
        tree = request.form.get("tree")
        if not name and not tree:
            message = "You didn't enter your name and number of trees"
        elif not name:
            message = "You didn't enter your name"
        elif not tree:
            message = "You didn't enter number of trees"
        else:
            db.execute(
                "INSERT INTO plantings (name, tree) VALUES(?, ?)",
                name,
                tree
            )
        plantings = db.execute("SELECT * FROM plantings")
        return render_template("index.html", message=message, plantings=plantings)

    else:

        # TODO: Display the entries in the database on index.html

        plantings = db.execute("SELECT * FROM plantings")
        return render_template("index.html", plantings=plantings)


