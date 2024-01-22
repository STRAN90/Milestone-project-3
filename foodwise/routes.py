from flask import render_template, request, redirect, url_for
from foodwise import app, db

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/sign_in")
def sign_in():
    return render_template("sign_in.html")


@app.route("/account")
def account():
    return render_template("account.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/add_recipe")
def add_recipe():
    return render_template("add_recipe.html")


@app.route("/edit_recipe")
def edit_recipe():
    return render_template("edit_recipe.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")

@app.route("/add_category")
def add_category():
    return render_template("add_category.html")


@app.route("/edit_category")
def edit_category():
    return render_template("edit_category.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")