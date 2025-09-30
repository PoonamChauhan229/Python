from flask import Flask,Blueprint,request,jsonify

blog_bp=Blueprint("blog","__name__")


@blog_bp.route('/home',methods=["GET"])
def home():
    return jsonify({"message":"Welcome to Blog App"})
@blog_bp.route('/blog',methods=["GET"])
def postBlog():
    return jsonify({"message":"This is the first Blog"})