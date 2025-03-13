import datetime
from flask import Flask, render_template, Response
import os.path

app = Flask(__name__)


def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):  # pragma: no cover
    try:
        src = os.path.join(root_dir(), filename)
        # Figure out how flask returns static files
        # Tried:
        # - render_template
        # - send_file
        # This should not be so non-obvious
        return open(src).read()
    except IOError as exc:
        return str(exc)


@app.route("/")
def index():  # pragma: no cover
    content = get_file("home.html")
    return Response(content, mimetype="text/html")


@app.route("/about")
def metrics():  # pragma: no cover
    content = get_file("about.html")
    return Response(content, mimetype="text/html")
