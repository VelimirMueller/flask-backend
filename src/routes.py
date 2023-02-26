from flask import request
from src import app
from src.helper.request import request_helper
from src.messages import msg_api
from flask_login import current_user, login_user
from src.helper.validator.schemas import USER_LOGIN_SCHEMA
import json

@app.route('/login', methods=['POST'])
def login():
    json_data = request.data.decode('utf-8')

    if current_user.is_authenticated:
        response = {
            msg_api['msg']: msg_api['logged_in']
        }
    else:
        response = request_helper(json_data, True, USER_LOGIN_SCHEMA)
        response_dict = json.loads(response.data.decode('utf-8'))
        
        if response_dict['status'] == "success":
            return response_dict['status']
        else:
            return response_dict