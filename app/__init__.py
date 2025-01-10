from dotenv import load_dotenv
load_dotenv(override=True)

from flask import Flask
from flask_migrate import Migrate #<-- Alembic and flask-migrate
from flask_sqlalchemy import SQLAlchemy

from .config import Config
from .routes import course_routes, lesson_routes, song_routes, user_routes, review_routes
from app.models import db #db object

import os

#Load environment variables
load_dotenv()

# Debug print to check if environment variables are loaded
print(f"DATABASE_URL from env: {os.environ.get('DATABASE_URL')}")

#Create Flask server
app = Flask(__name__)

#configurate the server with env variables
app.config.from_object(Config)

# Debug print to check if SQLALCHEMY_DATABASE_URI is set in app.config
print(f"SQLALCHEMY_DATABASE_URI in app.config: {app.config.get('SQLALCHEMY_DATABASE_URI')}")

# Ensure the SQLALCHEMY_DATABASE_URI is set
if not app.config.get('SQLALCHEMY_DATABASE_URI'):
    raise RuntimeError("SQLALCHEMY_DATABASE_URI is not set. Check your .env file.")


db.init_app(app) #<--Integrate flask, sqlalchemy
Migrate(app, db) #<--integrate flask,sqlalchemy, alembic
#Register blueprints


app.register_blueprint(course_routes.bp)
app.register_blueprint(lesson_routes.bp)
app.register_blueprint(user_routes.bp)
app.register_blueprint(song_routes.bp)
app.register_blueprint(review_routes.bp)


@app.route('/')
def home():
    return '<h1>Hello, World! its me</h1>  '
