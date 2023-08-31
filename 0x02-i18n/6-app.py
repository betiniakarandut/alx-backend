#!/usr/bin/env python3
"""Module for 6-app.py, templates/6-index.html"""
from flask import Flask, request, render_template, g
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """Returns user id if found"""
    if not user_id:
        return None
    return user_id


@app.before_request
def before_request():
    """Checks user info before any other
    request is processed
    """
    user_id = request.args.get('login_as')
    if user_id:
        user = get_user(int(user_id))
        if user:
            g.user = user


@app.route('/')
def index_6() -> str:
    """renders on a page best matching language"""
    return render_template('6-index.html', users=users)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
