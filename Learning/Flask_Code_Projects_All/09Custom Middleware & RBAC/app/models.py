from datetime import datetime

# User model
def user_model(username, password, role="user"):
    """Return a dictionary representing a new user"""
    return {
        "username": username,
        "password": password,  # hashed password
        "role": role,
        "created_at": datetime.utcnow()
    }

# Post model
def post_model(title, content, author_id):
    """Return a dictionary representing a new post"""
    return {
        "title": title,
        "content": content,
        "author_id": author_id,  # store ObjectId of user
        "created_at": datetime.utcnow()
    }