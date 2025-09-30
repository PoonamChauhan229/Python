from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId


auth_bp=Blueprint("auth",__name__)

@auth_bp.route('/',methods=["GET"])
def hello_world():
    return "Welcome to User Authentication"

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
        "password": hashed_password
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

    return jsonify({
        "message": "Login successful",
        "user_id": str(user["_id"])
    }), 200

