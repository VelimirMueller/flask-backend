from src.exceptions import api_exception
from src.messages import msg_api
from src.helper.validator import request_validator, schema_validator
from flask import jsonify

def request_helper(request, validateSchema=False, schema={} ):
    error_in_request_helper = False
    error_in_validator = False
    errors = []

    try:
        valid_json = eval(request)
        
    except Exception as err:
        error_in_request_helper = True
        valid_json = request
        errors.append({'request_helper_error': str(err)})

    try:
        valid_schema = schema_validator(valid_json['data'], validateSchema, schema)

        if request_validator(valid_json) == True and valid_schema['isValid'] == True or validateSchema == False:
            valid_json['status'] = "success"
            valid_json['response_message'] = "request can be processed"
        else:
            valid_json['status'] = 'error',
            valid_json['response_message'] = 'request could not pass validation gate'

            for key, value in valid_json['data'].items():
                valid_json['data'][str(key)] = "hashed value: " + str(hash(value))
    except Exception as err:
        error_in_validator = True
        errors.append({'validator_error': str(err)})

    if error_in_request_helper == False and error_in_validator == False:
        return jsonify({
            "data": valid_json['data'],
            "status": valid_json['status'],
            "type": 'API',
            "keys": len(valid_json['data']),
            "schema": valid_schema,
            "response_message": valid_json['response_message'],
            "requestHelperError": error_in_request_helper,
            "validatorError": error_in_validator
        })
    else:
        return jsonify({
            "error": "Critical processing error",
            "receivedData": valid_json,
            "errors": errors
        })