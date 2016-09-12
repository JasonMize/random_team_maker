from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.errorhandler(404)
def error_404(e):
    return "My bad"
