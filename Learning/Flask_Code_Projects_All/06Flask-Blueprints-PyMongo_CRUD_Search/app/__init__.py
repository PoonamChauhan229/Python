from flask import Flask
from .routes.blog import blog_bp
from .db import get_db

def createapp():
    app=Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/BluePrint-PyMongo-BLOG"
    app.mongo = get_db(app) # Initialize MongoDB and attach to app
    app.register_blueprint(blog_bp)
    return app