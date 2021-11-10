from flask import Flask, render_template
from templates import *

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to url shortener!"

@app.route('/shorten')
def shorten():
    return render_template('shorten.html')
    

if __name__ == '__main__':
    app.run(debug=True)

