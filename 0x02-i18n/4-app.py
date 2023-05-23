#!/usr/bin/env python3
"""
Set up a basic Flask app
"""
from flask import Flask, render_template, request
from flask_babel import Babel
from flask_babel import gettext as _


class Config:
    """
    Configure available languages in app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


config = Config()

app = Flask(__name__)
app.config.from_object(config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    determine the best match with our supported languages
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index() -> str:
    """
    Renders index template
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
