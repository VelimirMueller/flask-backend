from flask import request, jsonify, Response
from src import app, db
from src.helper.request import request_helper
from src.messages import msg_api
from flask_login import current_user, login_user, logout_user
from src.helper.validator.schemas import USER_LOGIN_SCHEMA
from src.models import User
import json

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

jwt = JWTManager(app)

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    message = str(current_user) + ' will be loggedout'
    logout_user()

    return jsonify({
        "response": message
    })

@app.route('/login', methods=['POST', 'GET'])
def login():
    access_token = False
    response_dict = request.data.decode('utf-8')

    if request.method == 'GET':
        if current_user.is_authenticated:
            response = {
                msg_api['msg']: msg_api['logged_in']
            }
            return response
        else:
            return 'PLEASE LOG IN FIRST !!!'

    if request.method == 'POST':
        try:
            json_data = request.data.decode('utf-8')
        except:
            json_data = eval(request.data)
            response_dict = json_data

            return response_dict

        if current_user.is_authenticated:
            response = {
                msg_api['msg']: msg_api['logged_in']
            }
            response_dict = response
        else:
            response = request_helper(json_data, True, USER_LOGIN_SCHEMA)
            response_dict = json.loads(response.data.decode('utf-8'))
            
        success = False
        try:
            if response_dict['status'] == "success":
                success = True
            else:
                success = False
        except:
            response_dict = eval(json_data)
            
            user = User.query.filter(
                    User.username.like(response_dict['username']),
                    User.password.like(response_dict['password'])
                ).first()
            if user:
                login_user(user, remember=True, force=True)
                access_token = create_access_token(identity=response_dict['username'])
                response_dict['browsertoken'] = access_token
                response_dict['currentuser'] = str(current_user)

            return response_dict
        
        if success == True:
            username = response_dict['data']['username']
            password = response_dict['data']['password']

            if username != "admin" or password != "password":
                response_dict['authentication'] = 'error - wrong credentials'
            else:
                response_dict['authentication'] = 'success'
                access_token = create_access_token(identity=username)
                response_dict['jwt-token'] = access_token
                user = User.query.filter(
                    User.username.like(username),
                    User.password.like(password)
                ).first()

                if user:
                    login_user(user, remember=True, force=True)
                    response_dict['current_user'] = str(current_user.get_id())
                    response_dict['jwt-token'] = access_token

            response_dict = Response(json.dumps(response_dict), 200)

    return response_dict