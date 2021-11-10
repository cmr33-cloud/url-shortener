from flask import Flask, render_template,request, redirect
import pyshorteners
import random

app = Flask(__name__)

def code():
    code = ""
    for i in range(5)
        lon = random.choice(range(2))
        if lon == 0:
            code 

alpha = 'abcdefghijklmnopqrstuvwxyz'


@app.route('/')
def welcome():
    return "Welcome to url shortener!"

@app.route('/shorten/', methods=['POST','GET'])
def shorten():
    if request.method == 'POST':
        url = request.form['url']
        s = pyshorteners.Shortener()
        shorten_url = s.tinyurl.short(url)
        print(shorten_url)
        return render_template('shorten.html', shorten_url = shorten_url)
    else:
        return render_template('shorten.html', shorten_url="")

    

if __name__ == '__main__':
    app.run(debug=True)
