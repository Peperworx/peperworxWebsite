from flask import Flask, render_template, request
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


app = CustomFlask(__name__)

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