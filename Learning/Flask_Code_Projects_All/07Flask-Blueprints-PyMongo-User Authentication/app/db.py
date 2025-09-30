from flask_pymongo import PyMongo
from flask import current_app

def get_db(app):   
    mongo = PyMongo(app)

    try:
        # Ping the database to check connection
        mongo.cx.admin.command('ping')
        print("✅ MongoDB connected successfully!")
    except:
        print("❌ MongoDB connection failed!")
    return mongo

#creating the instance and returning
