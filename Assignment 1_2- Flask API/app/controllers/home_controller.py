from flask import jsonify, request

from app.utilities.errors import BAD_REQUEST
from app.utilities.helpers import is_float



def sum_list_of_numbers():
    """Sum list of numbers and return the output
    :param json_body:
    :returns object:
    """
    
    ### validate request content-type
    if not request.is_json:
        return BAD_REQUEST("Invalid request")
    
    ### unpack request json
    data = request.json
    numbers = data.get("numbers")
    
    ### validate numbers list and return sum of numbers
    if isinstance(numbers, list) and all([is_float(number) for number in numbers]):
        floatNumbers = [float(number) for number in numbers] 
        return jsonify({ "result": sum(floatNumbers) })
    else:
        return BAD_REQUEST('key "numbers" must be list and must contains only digits')



def concat_two_strings():
    """Concat 2 string inputs
    :param json_body:
    :returns object:
    """

    ### validate request content-type
    if not request.is_json:
        return BAD_REQUEST("Invalid request")

    ### unpack request json
    data = request.json
    string1 = data.get("string1")
    string2 = data.get("string2")

    if not isinstance(string1, str) or not isinstance(string2, str):
        return BAD_REQUEST('keys "string1" and "string2" must be of type "string"')
    
    ### return response
    return jsonify({
        "result": string1 + " " + string2
    })