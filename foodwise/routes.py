from flask import render_template, request, redirect, url_for
from foodwise import app, db

@app.route("/")
def home():
    return "Hello world"