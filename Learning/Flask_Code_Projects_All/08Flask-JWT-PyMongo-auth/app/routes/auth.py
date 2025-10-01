from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId
from flask_jwt_extended import create_access_token,get_jwt_identity,jwt_required

auth_bp=Blueprint("auth",__name__)

@auth_bp.route('/test',methods=["GET"])
def hello_world():
    return "Welcome to User JWt Authentication"

# Register (Sign Up)
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    # Check if user already exists
    existing_user = current_app.mongo.db.users.find_one({"username": username})
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    # Hash password
    hashed_password = generate_password_hash(password)

    
    # Insert new user
    result = current_app.mongo.db.users.insert_one({
        "username": username,
        "password": hashed_password,
    })

    return jsonify({
        "message": "User registered successfully",
        "user_id": str(result.inserted_id)
    }), 201


# Login
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    user = current_app.mongo.db.users.find_one({"username": username})
    if not user:
        return jsonify({"error": "Invalid username or password"}), 401

    # Check hashed password
    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid username or password"}), 401

    # Generate JWT token
    token=create_access_token(identity=str(user["_id"]))

    return jsonify({
        "message": "Login successful",
        "user_id": str(user["_id"]),
        "token":token
    }), 200

# Test the JWT Token,
@auth_bp.route('/profile',methods=["GET"])
@jwt_required() ## this ensures only requests with a valid JWT can access
# Defines a new route
def profile():
    user_id=get_jwt_identity()
    print(user_id)
    user=current_app.mongo.db.users.find_one({"_id": ObjectId(user_id)},{"password":0})

    if not user:
        return jsonify({"error":"User Not Found"}),404
    user["_id"]=str(user["_id"])  # convert ObjectId to string
    return jsonify(user)