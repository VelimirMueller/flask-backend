from src.exceptions import api_exception
from src.messages import msg_api
from src.helper.validator import request_validator, schema_validator
from flask import jsonify

def request_helper(request, validateSchema=False, schema={} ):
    try:
        valid_json = eval(request)
        valid_schema = schema_validator(valid_json['data'], validateSchema, schema)

        if request_validator(valid_json) == True and valid_schema['isValid'] == True or validateSchema == False:
            valid_json['status'] = "success"
            valid_json['response'] = "request can be processed"
        else:
            valid_json['status'] = 'error',
            valid_json['response'] = 'request could not pass validation gate'

        return jsonify({
            "data": {"response": valid_json['response']},
            "status": valid_json['status'],
            "type": 'API',
            "keys": len(valid_json['data']),
            "schema": valid_schema
        })
    except: 
        invalid_json = {
            'error': api_exception(msg_api['data_invalid'], request),
            'status': 'error',
            'error_message': 'invalid syntax'
        }

        return jsonify({
            "status": invalid_json['status'],
            "error": invalid_json['error'],
            "error_message": invalid_json['error_message']
        })