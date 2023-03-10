import json
from src.exceptions import data_processing_exception
from src.messages import DATA_PROCESSING_MESSAGES

def json_normalizer(jsonData:dict) ->dict:
    try:
        # convert type to str or dict
        jsonData = jsonData.data.decode('utf-8')
    
        # If already dict type -> ready to process as dict/json
        if type(jsonData) is dict:
            return jsonData
        
        # If string -> load string as dict/json
        elif type(jsonData) is str: 
            return json.loads(jsonData)
    
    except Exception as err:
        return data_processing_exception(DATA_PROCESSING_MESSAGES['critical'], 500, str(err))


def transform_normalized_json(jsonData:dict) ->dict:
    try:
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
                'statusCode': 500
            }
            return jsonData
        
    except Exception as err:
        return data_processing_exception(DATA_PROCESSING_MESSAGES['critical'], 500, str(err))


def return_transformed_normalized_json(jsonData :dict) ->dict:
    try:
        normalizedJson = json_normalizer(jsonData)
        transformedNormalizedJson = transform_normalized_json(normalizedJson)

        return transformedNormalizedJson
    except Exception as err:
        return data_processing_exception(DATA_PROCESSING_MESSAGES['critical'], 500, str(err))
