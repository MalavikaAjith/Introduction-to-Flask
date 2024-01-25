from flask import Flask
app = Flask(__name__)

@app.route('/home/<int:age>')
def home(age):
    return "Age = %d"%age;
