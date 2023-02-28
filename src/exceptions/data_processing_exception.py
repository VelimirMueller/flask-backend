from src.exceptions.exception_error import exception_error

def data_processing_exception(error:str, statusCode:int, exception:str='did not intercept exception, please pass exception to data_processing_exception')->dict:
  return {
      'message': exception_error(error + ', statusCode: ' + str(statusCode)),
      'type': 'data_processing_exception',
      'status': 'error',
      'statusCode': statusCode,
      'exception': exception
    }