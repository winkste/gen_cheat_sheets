from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import os

# html page style website:
# https://getbootstrap.com/docs/5.1/getting-started/introduction/

# html form input type list:
# https://www.w3schools.com/html/html_form_input_types.asp


app = Flask(__name__)

# secret key is needed when using sessions
app.secret_key = "hello"
# lifetime of session data
app.permanent_session_lifetime = timedelta(minutes=5)

# sql database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


# start home page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods =["POST", "GET"])
def login():
    if request.method == "POST":
        # reset the session timeout
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user

        # search database by user name
        found_user =  users.query.filter_by(name = user).first()
        if found_user:
            session["email"] = found_user.email
        else:
            # generate a new user and commit to the db
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

        # message flashing
        flash(f"{user} sucessful logged in.", "info")
        # redirecting to new page user
        return redirect(url_for("user"))
    else:   
        # when clicking back to the login site, but still logged in
        if "user" in session:
            user = session["user"]
            flash(f"{user} already logged in", "info")
            return redirect(url_for("user")) 
        
        # not logged in, go to login
        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            found_user =  users.query.filter_by(name = user).first()
            found_user.email = email
            db.session.commit()
            flash("Email was saved")
        else:
            if "email" in session:
                email = session["email"]
        return render_template("user.html", email = email)
    else:
        flash(f"You are not logged in", "info")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        user = session["user"]
        flash(f"{user} have been logged out.", "info")
        # remove user from session
        session.pop("user", None)
        session.pop("email", None)
    else:
        flash("You are not privisously logged in.")
    return redirect(url_for("login"))

@app.route("/view")
def view():
    return render_template("view.html", values=users.query.all())

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

