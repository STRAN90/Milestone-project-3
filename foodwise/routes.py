from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from foodwise import app, db

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = Users.query.filter(Users.user_name ==
                                           request.form.get
                                           ("username").lower()).all()

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        user = Users(
            user_name=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )

        db.session.add(user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration complete")
        return redirect(url_for("profile", username=session["user"]))

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