from flask import Blueprint
from app.controllers.auth_controller import register_user, login_user


auth_bp = Blueprint("auth_bp", __name__)


auth_bp.route("/auth/register", methods=["POST"]) (register_user)
auth_bp.route("/auth/login", methods=["POST"])(login_user)