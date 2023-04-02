from flask import Blueprint, render_template, Flask
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)
# Defines Blueprint
views = Blueprint("views", __name__)

@views.route("/")
def home():
  return render_template("home.html")

if __name__ == '__main__':
    freezer.freeze()