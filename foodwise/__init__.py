import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    elif uri is None:
        # Handle the case where 'uri' is None, provide a default value or raise an exception
        raise RuntimeError("DATABASE_URL environment variable is not set.")
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)

from foodwise import routes  # noqa
