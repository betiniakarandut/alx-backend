#!/usr/bin/env python3
"""Module for 1-app.py, templates/1-index.html"""
from flask import Flask, render_template
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


@app.route('/')
def index_1() -> str:
    """renders a page with Language translation"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
