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