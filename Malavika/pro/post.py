from flask import Flask, request

app = Flask(__name__)
@app.route('/login', methods = ['POST'])
def login():
    uname = request.form['uname']
    pwd = request.form['pwd']
    if uname == "ch" and pwd == "google":
        return "Welcome "%uname