# save this as app.py
import datetime
from flask import Flask, render_template, Response
import os.path

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template(
        "index.html",
        utc_dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        something_text="本頁是首頁",
    )


@app.route("/about/")
def about():
    return render_template(
        "about.html",
        utc_dt="",
        something_text="這頁是關於的頁面",
    )


@app.route("/spider-result/")
def spider_result():

    content = get_file("./templates/spider-result.txt")
    # content = content.replace("\n", "<br>")
    return Response(content, mimetype="text/html")


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
