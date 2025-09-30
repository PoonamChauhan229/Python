from flask import Flask
from .db import get_db
from .routes.auth import auth_bp
from flask_jwt_extended import JWTManager

jwt = JWTManager() 
def createapp():
    app=Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/JWT-PyMongo-BLOG"
    app.config["JWT_SECRET_KEY"] = "supersecretjwt"
    app.mongo=get_db(app)
    app.register_blueprint(auth_bp)
    return app
