from flask import Flask,request
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Flask-PyMongo-CRUD-Queries"
mongo = PyMongo(app)

try:
    # Ping the database to check connection
    mongo.cx.admin.command('ping')
    print("✅ MongoDB connected successfully!")
except:
    print("❌ MongoDB connection failed!")

@app.route('/')
def hello_world():
    return {"test":"1234"}

@app.route('/adduser',methods=['POST'])
def createUser():
    data=request.json
    return data

@app.route(/)

if __name__=="__main__":
    app.run(debug=True)