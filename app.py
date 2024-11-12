# flask app where users can add, view, and delete contacts

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

contacts = []

@app.route("/")
def home():
    return render_template("/home.html")


@app.route("/show_contacts")
def showContacts():

    return render_template("/show_contacts.html", contacts = contacts)




@app.route("/add_contact")
def add_contact():
    return render_template("add_contact.html")

@app.route("/handleAddContact", methods=["POST"])
def handleAddContact(): #commit test2

    name = request.form.get("contact-name")
    number = request.form.get("contact-number")
    contacts.append([name,number])

    return render_template("/home.html")




@app.route("/delete_contact")
def delete_contact():

    return render_template("/delete_contact.html", contacts = contacts)

@app.route("/handleDeleteContact", methods=["POST"])
def handleDeleteContact():

    contactNumber = int(request.form.get("contact-number"))
    contacts.pop(contactNumber - 1)


    return render_template("/home.html")
    


if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")
