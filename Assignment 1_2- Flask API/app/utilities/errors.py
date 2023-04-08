from flask import Blueprint, jsonify
from werkzeug.exceptions import NotFound, HTTPException, Unauthorized
import traceback

"""Initialize blueprint"""
errors = Blueprint('errors', __name__)


"""Base Exception class"""
class BASE_EXCEPTION(Exception):

    def __init__(self, message=None, status_code=None, data={}):
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.data = data

    def to_dict(self):
        rv = { 'message': self.message, 'data': self.data }
        return rv


def BAD_REQUEST(message="Bad request", status_code=400, data={}):
    raise BASE_EXCEPTION(message, status_code, data)

def UNAUTHORIZED(message="Not authorized", status_code=401, data={}):
    raise BASE_EXCEPTION(message, status_code, data)

def FORBIDDEN(message="Access forbidden", status_code=403, data={}):
    raise BASE_EXCEPTION(message, status_code, data)

def NOT_FOUND(message="Not found", status_code=404, data={}):
    raise BASE_EXCEPTION(message, status_code, data)

def NOT_ACCEPTABLE(message="Access token is expired", status_code=406, data={}):
    raise BASE_EXCEPTION(message, status_code, data)

def UNHANDLED(message="Unhandled exception", status_code=500, data={}):
    print(message)
    raise BASE_EXCEPTION(message, status_code, data)


"""Handle user exections"""
@errors.app_errorhandler(BASE_EXCEPTION)
def base_exception_handler(e):
    return jsonify(e.to_dict()), e.status_code


"""Handle invalid http exceptions"""
@errors.app_errorhandler(HTTPException)
def internal_server_error(e):
    return jsonify({
        "message": e.description,
        "data": {}
    }), 500


"""Handle unhandled exceptions"""
@errors.app_errorhandler(Exception)
def other_exception(e):
    print(traceback.print_exc())
    return jsonify({
        "message": "Unhandled exception",
        "traceback": ''.join(traceback.TracebackException.from_exception(e).format())
    }), 500
