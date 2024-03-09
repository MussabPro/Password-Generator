from flask import Flask, redirect, render_template, request, session
import string
import random
app = Flask(__name__)

app.secret_key = "!<K-p<g!Cs'HElu`_8NwC)[]U7Pw'3l%->("


def Password_Generator(includeuppercase,
                       includelowercase,
                       includedight,
                       includesymbols, NumberofPasswords,
                       passwordlen):
    Uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    dights = string.digits
    symbols = string.punctuation
    CharValue = ""
    if includeuppercase == "y":
        CharValue += Uppercase
    if includelowercase == "y":
        CharValue += lowercase
    if includedight == "y":
        CharValue += dights
    if includesymbols == "y":
        CharValue += symbols
    return [
        "".join([random.choice(CharValue) for i in range(passwordlen)]) for x in range(NumberofPasswords)
    ]


@app.route('/password_generator', methods=['POST', 'GET'])
def password_generator():
    if request.method == 'POST':
        includeuppercase = request.form.get('includeuppercase')
        includelowercase = request.form.get('includelowercase')
        includedight = request.form.get('includedight')
        includesymbols = request.form.get('includesymbols')
        NumberofPasswords = request.form.get('NumberofPasswords')
        passwordlen = request.form.get('passwordlen')
        passwords = Password_Generator(includeuppercase,
                                       includelowercase,
                                       includedight,
                                       includesymbols, int(NumberofPasswords),
                                       int(passwordlen))
        if "passwords" in session:
            session.pop("passwords")
        session['passwords'] = passwords
        return redirect("/")
    return render_template("index.html")


@app.route('/')
def home():

    passwords = session.get("passwords", [])
    return render_template("index.html", passwords=passwords)
