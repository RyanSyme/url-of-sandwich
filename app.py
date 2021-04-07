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
    """
    Display index page.
    Fetch latest three sandwiches data from MongoDB sandwiches collection.
    Returns:
    template: index.html.
    """
    sandwiches = list(
                mongo.db.sandwiches.find().sort("_id", -1).limit(3))
    return render_template("index.html", sandwiches=sandwiches)


@app.route("/sandwiches")
def sandwiches():
    """
    Display sandwiches page.
    Query database for ingredients data from
    MongoDB sandwiches collection for search bar.
    Fetch full list of sandwiches in database
    Returns:
    template: sandwiches.html.
    """
    # search bar request
    query = request.args.get("query")
    if query:
        sandwiches = list(
            mongo.db.sandwiches.find({"$text": {"$search": query}}))
    else:
        # sort by time created
        sandwiches = list(mongo.db.sandwiches.find().sort("_id", -1))
    return render_template(
        "sandwiches.html", query=query, sandwiches=sandwiches)


@app.route("/view-sandwich/<sandwich_id>")
def view_sandwich(sandwich_id):
    """
    Display view_sandwich page.
    Fetch sandwich by database id from
    MongoDB sandwiches collection.
    Returns:
    template: view_sandwich.html.
    """
    sandwich = mongo.db.sandwiches.find_one({"_id": ObjectId(sandwich_id)})
    return render_template("view_sandwich.html", sandwich=sandwich)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """
    Displays signup page to guest user and allows account creation.
    Prevents username duplication by checking users.
    Stores details on MongoDB database in the users collection.
    Returns:
    template: redirect to profile.html if successful.
    template: signup.html if unsuccessful.
    """
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
    """
    Displays login page and allows user to log into account.
    Checks if the username exists in MongoDB users collection.
    Informs user if login is successful or not via flash messages.
    Returns:
    template: profile.html if login successful.
    template: login.html if unsuccessful.
    """
    if request.method == "POST":
        # check if username already in use
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # check hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash(
                            "Welcome, {}".format(request.form.get("username")))
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
    """
    Displays profile page, retreives session user's username from database.
    Checks previously submitted sandwiches by users username.
    Returns:
    template: profile.html if login successful.
    template: login.html if unsuccessful.
    """
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        # show sandwiches created by user in profile
        sandwiches = list(
            mongo.db.sandwiches.find({"created_by": username.lower()}))
        return render_template(
            "profile.html", username=username, sandwiches=sandwiches)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
    Removes session cookie.
    Shows flash message that logout has been successful.
    Returns:
    template: login.html.
    """
    flash("You have been logged out")
    # removes session cookies
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add-sandwich", methods=["GET", "POST"])
def add_sandwich():
    """
    Allows user to submit a sandwich to the website through a form.
    Allows form fields to be sent to the
    MongoDB sandwiches and category collection.
    Adds a new entry in to the collections.
    Returns:
    template: add_sandwich.html
    template: sandwiches.html after entires.
    """
    user = session.get("user").lower()
    if user is not None:
        if request.method == "POST":
            # add form info to database
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
    else:
        return render_template("403.html")


@app.route("/edit-sandwich/<sandwich_id>", methods=["GET", "POST"])
def edit_sandwich(sandwich_id):
    """
    Allows the user to edit their own submitted sandwiches through a form.
    Checks the sandwich ID field in MongoDB to fetch the data.
    Displays all previously entered data of the sandwich.
    Adds any changes made to the entries
    once submitted to the MongoDB collection.
    template: edit_sandwich.html.
    template: sandwiches.html after entires.
    """
    if request.method == "POST":
        # edit database record
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


@app.route("/delete-sandwich/<sandwich_id>")
def delete_sandwich(sandwich_id):
    """
    Allows user to delete sandwich.
    Deletes cocktail from database.
    Returns:
    template: redirects to sandwiches.html
    """
    mongo.db.sandwiches.remove({"_id": ObjectId(sandwich_id)})
    flash("Sandwich Successfully Removed")
    return redirect(url_for("sandwiches"))


@app.route("/category")
def category():
    """
    Display all categories (for admin only).
    Fetches a list of all categories in the MongoDB categories collection.
    Returns:
    template: categories.html
    """
    category = list(mongo.db.category.find().sort("category", 1))
    return render_template("category.html", category=category)


@app.route("/add-category",  methods=["GET", "POST"])
def add_category():
    """
    Allows admin to submit a category to the database through a form.
    Returns:
    template: add_categories.html
    template: categories.html after entry
    """
    if request.method == "POST":
        category = {
            "category": request.form.get("category")
        }
        mongo.db.category.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("category"))

    return render_template("add_category.html")


@app.route("/edit-category/<category_id>",  methods=["GET", "POST"])
def edit_category(category_id):
    """
    Allows the admin to edit a category through a form.
    Checks for category ID field in MongoDB to fetch relative data.
    Fetches changes to database and updates the collection.
    Checks if the user in session is the admin.
    template: edit_categories.html
    template: categories.html after entry
    """
    if request.method == "POST":
        submit = {
            "category": request.form.get("category")
        }
        mongo.db.category.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for('category'))

    category = mongo.db.category.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete-category/<category_id>")
def delete_category(category_id):
    """
    Allows admin to delete categories from database.
    Returns:
    template: redirects to categories.html
    """
    mongo.db.category.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("category"))


# Error handlers from flask documentation
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(403)
def access_denied(e):
    return render_template('403.html'), 403


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
