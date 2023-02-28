from src.helper.validator import request_validator
from src.helper.responses import return_success_response, return_error_response, return_error_response_dev
from src.messages import API_MESSAGES
import os

def request_helper(request:dict, validateSchema:bool=False , schema:dict={}):
    # Prepares request for processing and also validates if the request is in correct json format.
    # Can also validate the reuest schema fits into a defeined one in src/helper/validator/schema.
    # NOT RECOMMENDED: schema validation can be skipped but it comes in really handy to only process data which is essential.
    # Validating a schema has many pros, like forcing the developer to code more clean. But some people will not like it so
    # an option to disable schema validation but still keeping the API fully functional was implmeneted.
    if 'exception' in request['data']:
        if str(os.environ.get('DEV_MODE')) == '1':
            devDebugMsg = request['data']
            devDebugStatusCode = request['data']['statusCode']

            return return_error_response_dev(
                errorMessage=API_MESSAGES['invalidRequest'], 
                type=API_MESSAGES['requestType'], 
                statusCode=devDebugStatusCode, 
                devDebuggingMessage=devDebugMsg)
        
        return return_error_response(
            errorMessage=API_MESSAGES['invalidRequest'], 
            type=API_MESSAGES['requestType'], 
            statusCode=400)
        
    if request_validator(request) == True and schema['isValid'] == True or validateSchema == False:
        return return_success_response(
            successMessage=API_MESSAGES['validRequest'], 
            type=API_MESSAGES['requestType'], 
            keysInRequest=len(request['data']), 
            schema=schema)      
    else:
        return return_error_response(
            errorMessage=API_MESSAGES['invalidSchema'], 
            type=API_MESSAGES['schemaType'], 
            keysInRequest=len(request['data']), 
            schema=schema, 
            statusCode=400)