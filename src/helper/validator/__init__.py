def request_validator(jsonData) -> bool:
    if type(jsonData) is dict:
        return True
    else:
        return False
    
def schema_validator(jsonData, validateSchema=False, schema={}):
    if validateSchema == False:
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
    for key, val in schema.items():
        validSchema[key] = val
        schemaCache.append(key)
        schemaCache.sort()

    if(len(jsonCache) == len(schemaCache)):
        if(jsonCache == schemaCache):
            return {
                "status": 'schema is valid and has correct length',
                "isValid": True,
                "keys_received": str(jsonCache)
            }
        else:
            return {
                "status": 'invalid request keys - please check API schema for this request',
                "validSchema": str(validSchema),
                "isValid": False,
                "keys_received": str(jsonCache)
            }
    else:
        return {
                "status": 'schema has invalid length, allowed length: ' + str(len(schemaCache)),
                "isValid": False,
                "keys_received": str(jsonCache)
            }