from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
# Hash the password for more security
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

# Defines Blueprint
auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():

  # When submitting the form
  if request.method == "POST":
    email = request.form.get("email")
    password  = request.form.get("password")

    user = User.query.filter_by(email=email).first()
    if user:
      # If the password is the same:
      if check_password_hash(user.password, password):
        flash("Erfolgreich angemeldet", category="success")
        return redirect(url_for("views.home"))
      else:
        flash("Die eingegebenen Daten sind inkorrekt", category="error")
    else:
      flash("Diese E-Mail existiert nicht", category="error")


  return render_template("login.html", user="Christian", title="Login", boolean=True)

@auth.route("/logout")
def logout():
  return "<p>Logout</p>"

@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():

  if request.method == "POST":

    email = request.form.get("email")
    name = request.form.get("name")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")

    user = User.query.filter_by(email=email).first()
    # If email is already used:
    if user:
      flash("Ein Konto mit dieser E-Mail existiert bereits", category="error")
    elif len(email) < 4:
      flash("Ihre E-Mail-Adresse muss länger als 3 Zeichen sein", category="error")
    elif len(name) < 2:
      flash("Ihr vollständiger Name muss länger als 1 Zeichen sein", category="error")
    elif password1 != password2:
      flash("Bitte bestätigen Sie das eingegebene Passwort", category="error")
    elif len(password1) < 8:
      flash("Ihr Passwort muss mindestens aus 8 Zeichen bestehen", category="error")
    else:
      new_user = User(email=email, name=name, password=generate_password_hash(password1, method="sha256"))
      db.session.add(new_user)
      db.session.commit()

      flash("Erfolgreich registriert", category="success")

      return redirect(url_for("views.home"))
  
  return render_template("signup.html")
