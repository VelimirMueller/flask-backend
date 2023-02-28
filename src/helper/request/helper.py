from src.helper.validator import request_validator, schema_validator

def request_helper(request, validateSchema=False, schema={}):
    response_json = {}
    valid_json = {}

    if request == False:
        response_json['error'] = 'could not load json data - json request not in valid (stringified) json format'
        response_json['status'] = 'error'
        response_json['type'] = str(type(request))
        response_json['requestbody'] = str(request)
        response_json['status_code'] = 500
        
        return response_json
    
    # Make sure request is json and has data key
    if 'data' in request.keys():
        valid_json = request
    else:
        valid_json['data'] = request

    try:
        valid_schema = schema_validator(valid_json['data'], validateSchema, schema)
    except Exception as err:
        response_json['error'] = 'Could not validate schema!'
        response_json['status'] = 'error'
        response_json['exception'] = 'what error is this?' + str(err) + str(type(valid_json['data']))
        response_json['status_code'] = 500

        return response_json, 500

    if request_validator(valid_json) == True and valid_schema['isValid'] == True or validateSchema == False:
        response_json['data'] = valid_json['data']
        response_json['status'] = "ok"
        response_json['type'] = "API"
        response_json['#keys'] = len(valid_json['data'])
        response_json['schema'] = valid_schema
        response_json['status_code'] = 200
        
        return response_json    
    else:
        response_json['error'] = "Could not validate schema!"
        response_json['receivedData'] = valid_json['data']
        response_json['amount_of_keys'] = len(valid_json['data'])
        response_json['schema'] = valid_schema
        response_json['status_code'] = 500
        
        return response_json