import flask

app = flask.Flask(__name__)
visits = 0


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/counter")
def counter():
    global visits
    visits += 1
    return flask.render_template(
        "counter.html",
        visits=visits,
    )
