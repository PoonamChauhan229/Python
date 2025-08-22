from flask import Flask,request,jsonify

app=Flask(__name__)

users=[]

@app.route('/')
def hello_world():
    return jsonify({"message":"Welcome to App without DB performing CRUD",})

@app.route('/adduser',methods=['POST'])
def createUser():
    data=request.json
    users.append(data)
    return jsonify({"message":"User Created Succesfully","user":data})

@app.route('/getuser',methods=["GET"])
def getUsers():
    return jsonify(users)
    
@app.route('/updateUser/<name>',methods=["PUT"])
def updateUsers(name):
    data=request.json
    for user in users:
        if user.get('name')==name:
           user.update(data)
           return jsonify({"message":"User Updated","user":user})
    return jsonify({"error":"User Not Found"}) 

@app.route('/deleteUser/<name>',methods=["DELETE"])
def deleteUsers(name):
    for user in users:
        if user.get("name")==name:
            users.remove(user)
            return jsonify({"message":"User Deleted","user":user})
    return jsonify({"error":"User Not Found"})


if __name__=="__main__":
    app.run(debug=True) # if any error it will it will directly visible in browser