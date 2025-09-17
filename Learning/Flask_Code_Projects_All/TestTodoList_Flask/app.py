from flask import Flask,render_template,request,redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app=Flask(__name__)

# Mongo URL
client = MongoClient("mongodb://localhost:27017/")

# Access database and collection
db = client["mytodopython"]
collection = db["todos"]

 

@app.route('/')
def helloWorld():
    # return "hello, World"
    todos = list(collection.find())  # Fetch all todos
    return render_template("index.html", todos=todos)

@app.route('/add',methods=['POST'])
def addtodo():
    title=request.form['title']
    desc=request.form['desc']
    data={
        "title":title,
        "description":desc
    }

    if title and desc:
            collection.insert_one(data)
    return redirect('/')

@app.route('/delete',methods=['POST'])
def deleteTodos():
    id=request.form['id']
    collection.delete_one({"_id":ObjectId(id)})
    return redirect('/')


@app.route('/edit/<id>')
def editTodo(id):
    todo=collection.find_one({"_id":ObjectId(id)})
    return render_template("edit.html",todo=todo)

@app.route('/update/<id>',methods=['POST'])
def updateTodo(id):
    title=request.form['title']
    desc=request.form['desc']
    data={
        "title":title,
        "description":desc
    }
    collection.update_one({"_id":ObjectId(id)},{"$set":data})
    return redirect('/')

@app.route('/products')
def products():
    return "Hi, Welcome to products Page"

if __name__=="__main__":
    app.run(debug=True,port=8000) # if any error it will it will directly visible in browser