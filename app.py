import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/index")
def index():
    sandwiches = list(
                mongo.db.sandwiches.find(
                    {"created_by": "earlofsandwich"}).limit(3))
    return render_template("index.html", sandwiches=sandwiches)


@app.route("/sandwiches")
def sandwiches():
    sandwiches = list(mongo.db.sandwiches.find().sort("sandwich_name", 1))
    return render_template("sandwiches.html", sandwiches=sandwiches)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    sandwiches = list(mongo.db.sandwiches.find({"$text": {"$search": query}}))
    return render_template("sandwiches.html", sandwiches=sandwiches)


@app.route("/view_sandwich/<sandwich_id>")
def view_sandwich(sandwich_id):
    sandwich = mongo.db.sandwiches.find_one({"_id": ObjectId(sandwich_id)})
    return render_template("view_sandwich.html", sandwich=sandwich)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if username already in use
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(signup)

        # put new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username already in use
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(request.form.get("username")))
                        return redirect(
                            url_for("profile", username=session["user"]))
            else:
                # Wrong password
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # retreive session user's username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        sandwiches = list(
            mongo.db.sandwiches.find({"created_by": username.lower()}))
        return render_template(
            "profile.html", username=username, sandwiches=sandwiches)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_sandwich", methods=["GET", "POST"])
def add_sandwich():
    if request.method == "POST":
        sandwiches = {
            "sandwich_name": request.form.get("sandwich_name"),
            "description": request.form.get("description"),
            "category": request.form.get("category"),
            "prep_time": request.form.get("prep_time"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        mongo.db.sandwiches.insert_one(sandwiches)
        flash("Sandwich Successfully Added")
        return redirect(url_for("sandwiches"))

    category = mongo.db.category.find().sort("category", 1)
    return render_template("add_sandwich.html", category=category)


@app.route("/edit_sandwich/<sandwich_id>", methods=["GET", "POST"])
def edit_sandwich(sandwich_id):
    if request.method == "POST":
        submit = {
            "sandwich_name": request.form.get("sandwich_name"),
            "description": request.form.get("description"),
            "category": request.form.get("category"),
            "prep_time": request.form.get("prep_time"),
            "ingredients": request.form.get("ingredients"),
            "instructions": request.form.get("instructions"),
            "image_url": request.form.get("image_url"),
            "created_by": session["user"]
        }
        mongo.db.sandwiches.update({"_id": ObjectId(sandwich_id)}, submit)
        flash("Sandwich Successfully Updated")
        return redirect(url_for("sandwiches"))

    sandwich = mongo.db.sandwiches.find_one({"_id": ObjectId(sandwich_id)})
    category = mongo.db.category.find().sort("category", 1)
    return render_template(
        "edit_sandwich.html", sandwich=sandwich, category=category)


@app.route("/delete_sandwich/<sandwich_id>")
def delete_sandwich(sandwich_id):
    mongo.db.sandwiches.remove({"_id": ObjectId(sandwich_id)})
    flash("Sandwich Successfully Removed")
    return redirect(url_for("sandwiches"))


@app.route("/category")
def category():
    category = list(mongo.db.category.find().sort("category", 1))
    return render_template("category.html", category=category)


@app.route("/add_category",  methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category": request.form.get("category")
        }
        mongo.db.category.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("category"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>",  methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "category": request.form.get("category")
        }
        mongo.db.category.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for('category'))

    category = mongo.db.category.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.category.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("category"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
