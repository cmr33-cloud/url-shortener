from flask import Flask, render_template,request, redirect, url_for
import pyshorteners
import random
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#needed to use the sqlalchemy - url is the table name
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///url.db'
app.config["SQLAlchemy_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

class url(db.Model):
    _id = db.Column("id",db.Integer,primary_key=True)
    url = db.Column(db.String(100))
    shortened_url = db.Column(db.String(100))

    def __init__(self,url,shortened_url):
        self.url = url
        self.shortened_url = shortened_url

alpha = 'abcdefghijklmnopqrstuvwxyz'

def code():
    code = ""
    for i in range(5):
        lon = random.choice(range(2))
        if lon == 0:
            uol = random.choice(range(2))
            if uol == 0:
                code += random.choice(alpha).upper()
            else:
                code += random.choice(alpha)
        else:
            code += str(random.choice(range(10)))
    return code 


# @app.route('/')
# def welcome():
#     return "Welcome to url shortener!"

@app.route('/', methods=['POST','GET'])
def url_shortener():
    if request.method == 'POST':
        user_url = request.form['url']
        # s = pyshorteners.Shortener()
        # shorten_url = s.tinyurl.short(user_url)
        shorten_url = code()
        # print(f"short url  {shorten_url}")
        new_url = url(url=user_url,shortened_url=shorten_url)
        db.session.add(new_url)
        db.session.commit()
        return render_template('shorten.html', shorten_url = "http://127.0.0.1:5000/"+shorten_url)
    else:
        return render_template('shorten.html', shorten_url="")

@app.route('/<userURL>',methods=['GET'])
def redirect_newurl(userURL):
    long_url = url.query.filter_by(shortened_url=userURL).first()
    # print(f"long url {long_url.url}")
    if long_url:
        print(f"long url: {long_url.url}")
        url_http = "https://" + long_url.url
        return redirect(url_http)
        
    else:
        print("after else")
        return "not found"
        
    

if __name__ == '__main__':
    app.run(debug=True)
