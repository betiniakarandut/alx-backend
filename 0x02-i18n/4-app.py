#!/usr/bin/env python3
"""Module for 4-app.py, templates/4-index.html"""
from flask import Flask, request, render_template
from flask_babel import Babel


class Config:
    """default language config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

# Instantiates Babel class
babel = Babel(app)


@babel.localeselector
def get_locale():
    """gets best matching language"""
    if 'locale' in request.args:
        locale = request.args['locale']
        if locale in app.config["LANGUAGES"]:
            return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index_4() -> str:
    """renders on a page best matching language"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
