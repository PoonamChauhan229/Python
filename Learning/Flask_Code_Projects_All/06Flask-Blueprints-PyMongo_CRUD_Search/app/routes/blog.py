from flask import Flask,Blueprint,jsonify,request,current_app
from bson.objectid import ObjectId



# current_app Access Flask app instance anywhere inside routes/blueprints
blog_bp=Blueprint("blog",__name__)

@blog_bp.route("/home",methods=["GET"])
def bloghome():
    return "Welcome to the Blueprint Page Testing Route"

# Create
@blog_bp.route('/blog',methods=["POST"])
def create_blog():
    data=request.json
    result= current_app.mongo.db.blog.insert_one(data)
    blog=current_app.mongo.db.blog.find_one({"_id":result.inserted_id})
    return jsonify({
        "message":"Blog Created Successfully",
        "blog":blog,
        "blog_id": str(result.inserted_id)
        })

# Read
@blog_bp.route('/blog',methods=["GET"])
def get_blogs():
    blogs=current_app.mongo.db.blog.find()
    # return jsonify(users)
    return jsonify(list(blogs))

@blog_bp.route('/blog/<id>',methods=['GET'])
def fetSingleUser(id):
    blog=current_app.mongo.db.users.find_one({"_id":ObjectId(id)})
    return jsonify(blog)

# Update
@blog_bp.route('/blog/<id>',methods=["PUT"])
def update_blogs():
    data=request.json
    current_app.mongo.db.users.update_one({"_id":ObjectId(id)},{"$set":data})
    return jsonify({"message":"User Updated Successfully"})


# Delete
@blog_bp.route('/blog/<id>',methods=["DELETE"])
def delete_blogs():
    current_app.mongo.db.blog.delete_one({"_id":ObjectId(id)})
    return jsonify({"message":"User Deleted Successfully"})

# Search
@blog_bp.route('/blog/search', methods=["GET"])
def search_blogs():
    title = request.args.get("title", "")
    blogs = list(current_app.mongo.db.blog.find({"title": title}))
    return jsonify(blogs)  # response shown in browser/Postman

