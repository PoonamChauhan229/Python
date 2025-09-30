from flask import Flask
from .routes.blog import blog_bp


def creatapp():
    app=Flask(__name__)
    # app.register_blueprint(blog_bp,url_prefix="/blog")
    app.register_blueprint(blog_bp)
    return app


