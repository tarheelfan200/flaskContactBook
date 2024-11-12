# flask app where users can add, view, and delete contacts

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

contacts = []

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add_contact")
def add_contact():
    return render_template("add_contact.html")

@app.route("/handleAddContact", methods=["POST"])
def handleAddContact():

    name = request.form.get("contact-name")
    number = request.form.get("contact-number")
    contacts.append([name,number])

    return render_template("/show_contacts.html", x = name, y = number)

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
