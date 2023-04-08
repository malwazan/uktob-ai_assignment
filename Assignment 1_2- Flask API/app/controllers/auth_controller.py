from flask import request, jsonify

from app.utilities.errors import BAD_REQUEST, UNAUTHORIZED
from app.services.auth_service import AuthService


def register_user():
    """Register new user
    :param json_body:
    :returns object:
    """

    ### validate request content-type
    if not request.is_json:
        return BAD_REQUEST("Invalid request")
    
    ### unpack request json
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not isinstance(username, str) or not isinstance(password, str):
        return BAD_REQUEST('Invalid "username" or "password"')
    
    if not AuthService.validate_unique_username(username):
        return BAD_REQUEST('"username" is already registered')
    
    if not AuthService.validate_password(password):
        return BAD_REQUEST('"password" must be atleast 4 characters in length')
    
    ### register new user
    response = AuthService.register_user(username, password)
    
    ### return response
    return jsonify({ "message": "user registered" }), 201


def login_user():
    """Login user
    :param json_body:
    :returns object:
    """

    ### validate request content-type
    if not request.is_json:
        return BAD_REQUEST("Invalid request")
    
    ### unpack request json
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not isinstance(username, str) or not isinstance(password, str):
        return BAD_REQUEST('Invalid "username" or "password"')
    
    ### login user
    response = AuthService.login_user(username, password)

    ### return response
    if not response:
        return UNAUTHORIZED('Invalid "username" or "password"')
    else:
        return jsonify({ "message": "user logged-in"})

