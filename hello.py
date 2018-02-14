import flask

app = flask.Flask(__name__)
visits = 0


@app.route("/")
def index():
    return "Hello World!"


@app.route("/counter")
def counter():
    global visits
    visits += 1
    return flask.render_template(
        "counter.html",
        visits=visits,
    )


@app.route("/hello/<name>")
def hello(name):
    name = name.capitalize()
    return flask.render_template(
        "hello.html",
        name=name,
    )
