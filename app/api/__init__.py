from flask import Blueprint

api = Blueprint('api', __name__)

def initialize_api():
    from . import authentication, posts, users, comments, errors

initialize_api()
