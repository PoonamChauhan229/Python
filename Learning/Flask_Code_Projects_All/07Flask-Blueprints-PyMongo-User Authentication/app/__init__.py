from flask import Flask
from .routes.auth import auth_bp
from .db import get_db

def createapp():
    app=Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/BluePrint-PyMongo-BLOG"
    app.mongo = get_db(app) # Initialize MongoDB and attach to app
    app.register_blueprint(auth_bp)
    return app