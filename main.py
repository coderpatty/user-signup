from flask import Flask, request, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('helloform.html', title='Sign-Up')

@app.route("/hello", methods=['POST'])
def hello():
    username = request.form['username']
    password = request.form["password"]
    verifypassword = request.form["verifypassword"]
    email = request.form["email"]

    username_error = verifyusername(username)
    password_error, verifypassword_error = verifypasswords(password, verifypassword)
    email_error = verifyemail(email)

    if not username_error and not password_error and not email_error:
        return render_template('welcome.html', title='Sign-Up', username=username)
    else:
        return render_template("helloform.html", title='Sign-Up', 
            username=username, 
            username_error=username_error,
            password="", 
            password_error = password_error,
            verifypassword="", 
            verifypassword_error = verifypassword_error,
            email=email, 
            email_error=email_error,
            )

def verifyusername(username):
    username_error = ""

    if username == "":
        username_error = "Enter a Username"

    if len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 - 20 characters"

    return username_error

def verifypasswords(password, verifypassword):
    password_error = ""
    verifypassword_error = ""

    if password == "":
        password_error = "Enter a Password"

    if len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 - 20 characters"

    if verifypassword == "":
        verifypassword_error = "Verify Password"

    if password != verifypassword:
        password_error = "Passwords must match"

    return password_error, verifypassword_error

def verifyemail(email):
    return ""
    
app.run()