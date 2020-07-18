#! /usr/bin/python3
from flask import Flask, render_template, request, Response, session, \
    flash, url_for, make_response, send_file
from api import sessions
from http import cookies
import pymongo
import json
import requests

class CustomFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    #jinja_options.update(dict(
    #block_start_string='$$',
    #block_end_string='$$',
    #variable_start_string='$',
    #variable_end_string='$',
    #comment_start_string='$#',
    #comment_end_string='#$',
    #))

config = json.load(open("../config.json","r"))


app = CustomFlask(__name__)

app.secret_key = b'\xc7\xcb\xff\xee\xd3\xd6\x00\x9en\xf3\xc9\xe2[b\xaa\xe8'

mongoCli = pymongo.MongoClient(config["mongoDB"])

app.config.from_object(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/launcher")
def launcher():
    return render_template("launcher.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/session")
def sessionGetter():
    sess = sessions.Session(mongoCli)
    C = cookies.SimpleCookie(request.cookies)

    sess.load(C["session"].value)

    return sess.dictionary

@app.route("/favicon.ico")
def favicon():
    return send_file("static/img/logo.jpg")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80, debug=True)