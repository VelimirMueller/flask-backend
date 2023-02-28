import json

def json_normalizer(json_data):
    try:
        # convert type to str or dict
        usable_data_format = json_data.data.decode('utf-8')
    
        # If already dict type -> ready to process as dict/json
        if type(usable_data_format) is dict:
            return usable_data_format
        
        # If string -> load string as dict/json
        elif type(usable_data_format) is str: 
            return json.loads(usable_data_format)
        
        # Wrong type will fail in request_helper()
        else:
            return str(type(json_data))
    
    except:
        return False
