from flask import Flask, render_template, request, Response, session, \
    flash, url_for, make_response
from flask_session import Session
import requests

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
    block_start_string='$$',
    block_end_string='$$',
    variable_start_string='$',
    variable_end_string='$',
    comment_start_string='$#',
    comment_end_string='#$',
    ))

config = json.load(open("../config.json","r"))


app = CustomFlask(__name__)

app.secret_key = b'\xc7\xcb\xff\xee\xd3\xd6\x00\x9en\xf3\xc9\xe2[b\xaa\xe8'
SESSION_TYPE = 'mongodb'
mongoCli = pymongo.MongoClient(config["mongoDB"])
SESSION_MONGODB = mongoCli
SESSION_MONGODB_DB= "flaskSessions"
app.config.from_object(__name__)
Session(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/launcher")
def launcher():
    return render_template("launcher.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/loginuser", methods=["POST"])
def loginUser():
    username = request.values.get("user")
    password = request.values.get("pass")
    redirect = request.values.get("redirect")
    url = 'http://localhost:8000/users/'+username
    myobj = {'password':password}

    x = requests.post(url, data = myobj)
    if redirect != None:
        pass
    return x.text


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80, debug=True)