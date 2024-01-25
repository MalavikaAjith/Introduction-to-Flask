from flask import Flask
app = Flask(__name__)
@app.route('/home/<name>')
def home(name):
    return "hello,"+name;
