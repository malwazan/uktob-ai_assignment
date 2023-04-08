from flask import Blueprint
from app.controllers.home_controller import sum_list_of_numbers, concat_two_strings


home_bp = Blueprint("home_bp", __name__)



home_bp.route("/home/sum", methods=["POST"]) (sum_list_of_numbers)
home_bp.route("/home/concat", methods=["POST"]) (concat_two_strings)