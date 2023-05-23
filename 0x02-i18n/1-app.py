#!/usr/bin/env python3
"""
Set up a basic Flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Configure available languages in app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


config = Config()

app = Flask(__name__)
babel = Babel(app)
app.config.from_object(config)


@app.route("/", strict_slashes=False)
def index():
    """
    Renders index template
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
