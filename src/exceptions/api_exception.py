from src.exceptions.exception_error import exception_error

def api_exception(error:str, statusCode:int)->dict:
  
  return {
    'message': exception_error(error + ', statusCode: ' + str(statusCode)),
    'type': 'api_exception',
    'status': 'error',
    'statusCode': statusCode
  }