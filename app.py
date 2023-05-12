from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {"name":"nikhl Walia","gender":"male"}

@app.route("/about")
def about():
    return "About Page"