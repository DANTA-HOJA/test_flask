from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, flask"

@app.route("/data")
def handleData():
    return "My Data"

@app.route("/user/<username>")
def handleUser(username):
    if username == "安安":
        return "你好， " + username
    return "Hello, " + username

app.run(debug=True, port=3000)