from flask import Blueprint, render_template, request, flash

# Defines Blueprint
auth = Blueprint("auth", __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
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

    if len(email) < 4:
      flash("Ihre E-Mail-Adresse muss länger als 3 Zeichen sein", category="error")
    elif len(name) < 2:
      flash("Ihr vollständiger Name muss länger als 1 Zeichen sein", category="error")
    elif password1 != password2:
      flash("Bitte bestätigen Sie das eingegebene Passwort", category="error")
    elif len(password1) < 8:
      flash("Ihr Passwort muss mindestens aus 8 Zeichen bestehen", category="error")
    else:
      flash("Erfolgreich registriert", category="success")
  
  return render_template("signup.html")
