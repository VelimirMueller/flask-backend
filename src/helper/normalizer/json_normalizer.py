import json
from src.exceptions import api_exception

def json_normalizer(jsonData):
    try:
        # convert type to str or dict
        jsonData = jsonData.data.decode('utf-8')
    
        # If already dict type -> ready to process as dict/json
        if type(jsonData) is dict:
            return jsonData
        
        # If string -> load string as dict/json
        elif type(jsonData) is str: 
            return json.loads(jsonData)
        
        # Wrong type will fail in request_helper()
        else:
            return False
    
    except:
        return False


def transform_normalized_json(jsonData):
        if jsonData != False:
            newJson = {}
             # Make sure request is json and has data key otherwise creates a data key and tries to validate request.
            if 'data' in jsonData.keys():
                return jsonData
            else:
                newJson['data'] = jsonData

            return newJson         
        else:
            jsonData = {
                'data': False,
                'statusCode': 400
            }
            return jsonData


def return_transformed_normalized_json(jsonData):
    normalizedJson = json_normalizer(jsonData)
    transformedNormalizedJson = transform_normalized_json(normalizedJson)

    return transformedNormalizedJson
