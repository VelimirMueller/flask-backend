import os, json

def return_success_response(successMessage, type, keysInRequest, schema):
    return {
        'successMessage': successMessage,
        'status': 'success',
        'type': type,
        'keysInRequest': keysInRequest,
        'schema': schema,
        'statusCode': 200
    }

def return_error_response(errorMessage, type='error type was not set', keysInRequest='not checked', schema='not checked', statusCode=400):
    return {
        'errorMessage': errorMessage,
        'status': 'error',
        'type': type,
        'schema': schema,
        'keysInRequest': keysInRequest,
        'statusCode': statusCode
    }

def return_error_response_dev(errorMessage, type='error type was not set', keysInRequest='not checked', schema='not checked', statusCode=400, isDevMode=False, devDebuggingMessage='dev mode not active - pls set DEV_MODE=1 in .flaskenv'):
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