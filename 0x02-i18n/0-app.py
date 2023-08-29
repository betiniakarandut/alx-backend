#!/usr/bin/env python3
"""Module for 0-app.py"""
from flask import Flask, render_template

app = Flask(__name__)

# Render a basic flask app
@app.route('/')
def index_0() -> str:
    return render_template(f'0-index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
