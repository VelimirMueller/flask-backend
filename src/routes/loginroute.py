from flask import request
from src import app
from src.helper.request import request_helper
from src.helper.normalizer import return_transformed_normalized_json
from src.helper.validator import schema_validator
from src.helper.validator.schemas import USER_LOGIN_SCHEMA

@app.route('/login', methods=['POST', 'GET'])
def login()->dict:
    # Login API endpoint with schema validation.
    # Returns a json response after receiving a request at /login.
    # TODO: implement jwt authentication and oAuth and set remember cookie
    processableRequest = return_transformed_normalized_json(request)
    
    processedSchema = schema_validator(
        processableRequest['data'], 
        validateSchema=True, 
        useSchema=USER_LOGIN_SCHEMA)
    
    response = request_helper( 
        request=processableRequest, 
        validateSchema=True, 
        schema=processedSchema)

    return response, response['statusCode']
   

    