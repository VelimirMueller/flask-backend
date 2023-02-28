from flask import request, jsonify
from src import app
from src.helper.request import request_helper
from src.helper.normalizer import json_normalizer
from src.helper.validator.schemas import USER_LOGIN_SCHEMA


@app.route('/login', methods=['POST', 'GET'])
def login():
    response = request_helper(request=json_normalizer(request), validateSchema=True, schema=USER_LOGIN_SCHEMA)
    
    return jsonify({
        "response": response
    }), response['status_code']