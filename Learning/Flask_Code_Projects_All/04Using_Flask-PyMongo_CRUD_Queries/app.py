from flask import Flask,request,jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

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
    """
    Simple test route for the Flask app.

    Returns a JSON object with a single key-value pair.

    Example Response:
    {
        "test": "1234"
    }
    """

    return {"test":"1234"}

@app.route('/adduser',methods=['POST'])
def createUser():
    # return request.json
    data=request.json
    result= mongo.db.users.insert_one(data)
    user=mongo.db.users.find_one({"_id":result.inserted_id})
    return jsonify({
        "message":"User Created Successfully",
        "user":user,
        "user_id": str(result.inserted_id)
        })

@app.route('/getusers',methods=['GET'])
def getUsers():
    users=mongo.db.users.find()
    # return jsonify(users)
    return jsonify(list(users))

@app.route('/getuser/<id>',methods=['GET'])
def fetSingleUser(id):
    user=mongo.db.users.find_one({"_id":ObjectId(id)})
    return jsonify(user)

@app.route('/deleteuser/<id>',methods=['DELETE'])
def deleteUser(id):
    mongo.db.users.delete_one({"_id":ObjectId(id)})
    return jsonify({"message":"User Deleted Successfully"})

@app.route('/updateuser/<id>',methods=['PUT'])
def updateUser(id):
    data=request.json
    mongo.db.users.update_one({"_id":ObjectId(id)},{"$set":data})
    return jsonify({"message":"User Updated Successfully"})

if __name__=="__main__":
    app.run(debug=True)