from flask import Blueprint, render_template


main = Blueprint("main", __name__, url_prefix='')


@main.route("/")
def home() -> str:
    return render_template("home.html")
