def request_validator(jsonData:dict)->bool:
    # Checks if a request is in valid json format and returns True/False.
    if type(jsonData) is dict or type(jsonData) is str:
        return True
    else:
        return False

    
def schema_validator(jsonData:dict, validateSchema:bool=False, useSchema:dict={})->dict:
    # Validates a request schema with a static defined one in src/helper/validator/schemas.
    # Returns a json response which will be further processed in request_helper(). When setting validateSchema to False
    # the schema validation part will be skipped and the request will be processed. 
    # WARNING: Setting validateSchema=False can lead to unwanted behaviour. 
    # Make sure your endpoint can handle unvalidated schemas.
    if validateSchema == False or jsonData == False:
        return {
            "status": 'Schema was not validated - please make sure you know what you are doing or enable schema validation in request_helper()!',
            'isValid': 'undefined'
        }
    jsonCache = []
    schemaCache = []
    validSchema = {}

    for key, val in jsonData.items():
        jsonCache.append(key)
        jsonCache.sort()
        
    for key, val in useSchema.items():
        validSchema[key] = val
        schemaCache.append(key)
        schemaCache.sort()

    if(len(jsonCache) == len(schemaCache)):
        if(jsonCache == schemaCache):
            return {
                "status": 'schema is valid and has correct length',
                "isValid": True,
                "keys_received": str(jsonCache),
                "keys_in_schema": len(schemaCache)
            }
        else:
            return {
                "status": 'invalid request keys - please check API schema for this request',
                "validSchema": str(validSchema),
                "isValid": False,
                "keys_received": str(jsonCache),
                "keys_in_schema": len(schemaCache)
            }
    else:
        return {
                "status": 'schema has invalid length, allowed length: ' + str(len(schemaCache)),
                "isValid": False,
                "keys_received": str(jsonCache),
                "validSchema": str(validSchema),
                "keys_in_schema": len(schemaCache)
            }