def exception_error(error):
  exception = {}
  exception['error'] = error

  return exception

def api_exception(error, objectType):
  exception = exception_error(error + ", type of data: " + str(type(objectType)))
  exception['type'] = 'API'

  return {
    'exception': exception
  }