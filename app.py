# flask app where users can add, view, and delete contacts

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add_contact.html")
def add_contact():
    return render_template("add_contact.html")

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
