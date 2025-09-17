from flask import Flask,render_template,redirect
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Flask-PyMongo"
mongo = PyMongo(app)

try:
    # Ping the database to check connection
    mongo.cx.admin.command('ping')
    print("✅ MongoDB connected successfully!")
except:
    print("❌ MongoDB connection failed!")

@app.route('/')
def hello_world():
    # todos=mongo.db.find()
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)