from flask import Flask
from selenium import webdriver  # noqa

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, asdfasdf!"


app.run(debug=True)
