import os
from typing import Union

def return_success_response(successMessage:str, type:str, keysInRequest:int, schema:dict)->dict:
    # Returns a normalized success response in json format. This way the shema of responses are always the same which should be a big plus while developing.
    return {
        'successMessage': successMessage,
        'status': 'success',
        'type': type,
        'keysInRequest': keysInRequest,
        'schema': schema,
        'statusCode': 200
    }

def return_error_response(errorMessage:str, type:str='error type was not set', keysInRequest:Union[int, str]='not checked', schema:Union[int, str]='not checked', statusCode:int=400)->dict:
    # Returns a normalized success response in json format. This way the shema of responses are always the same which should be a big plus while developing.
    return {
        'errorMessage': errorMessage,
        'status': 'error',
        'type': type,
        'schema': schema,
        'keysInRequest': keysInRequest,
        'statusCode': statusCode
    }

def return_error_response_dev(errorMessage:str, type:str='error type was not set', keysInRequest:Union[int, str]='not checked', schema:Union[bool, str]='not checked', statusCode:int=400, isDevMode:bool=False, devDebuggingMessage:Union[bool, str]='dev mode not active - pls set DEV_MODE=1 in .flaskenv')->dict:
    # Returns like return_error_response an normalized response. The only difference occurs when setting DEV_MODE=1 in .flaskenv.
    # This way the response will contain a dev debugging message, containing the exception message
    if str(os.environ.get('DEV_MODE')) == "1":
        isDevMode = True
        devDebuggingMessage = devDebuggingMessage
    return {
        'devDebuggingMessage': devDebuggingMessage,
        'isDevMode': isDevMode,
        'errorMessage': errorMessage,
        'status': 'error',
        'type': type,
        'schema': schema,
        'keysInRequest': keysInRequest,
        'statusCode': statusCode
    }