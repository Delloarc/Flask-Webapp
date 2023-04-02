# This __init__.py makes the website folder a package
# In CMD install flask, flask-login and flask-sqlalchemy

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Defining a database

db = SQLAlchemy()
DB_NAME = "database.db"

# Initializes Flask
def create_app():
  app = Flask(__name__)
  # Secret key can be anything, don't share with people
  app.config["SECRET_KEY"] = "This is my secret key"
  # SQLALCHEMY database is stored here
  app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite///{DB_NAME}"
  db.init_app(app)

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix="/")
  app.register_blueprint(auth, url_prefix="/")

  return app
  