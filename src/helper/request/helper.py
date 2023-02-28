from src.helper.validator import request_validator, schema_validator
from src.helper.responses import return_success_response, return_error_response
from src.exceptions import api_exception
from src.messages import API_MESSAGES

def request_helper(request, validateSchema=False, schema={}):
    if request['data'] == False:
        return return_error_response(errorMessage=API_MESSAGES['invalidRequest'], type=API_MESSAGES['requestType'], statusCode=400)
        
    if request_validator(request) == True and schema['isValid'] == True or validateSchema == False:
        return return_success_response(successMessage=API_MESSAGES['validRequest'], type=API_MESSAGES['requestType'], keysInRequest=len(request['data']), schema=schema)      
    else:
        return return_error_response(errorMessage=API_MESSAGES['invalidSchema'], type=API_MESSAGES['schemaType'], keysInRequest=len(request['data']), schema=schema, statusCode=400)