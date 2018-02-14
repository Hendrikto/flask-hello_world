from flask import Flask
app = Flask(__name__)

visits = 0


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/counter")
def counter():
    global visits
    visits += 1
    return f"<b>Visits:</b> {visits}"
