# Schemas are being used to compare request.data with API scheme for endpoint.
# Only process the request if requst.data has the correct data scheme.
# Will be processed by schema_validator() of src.helper.validator.schema.__init__,py
#
# Add schemas in src.helper.validator.schemas.__init__.py - from src.helper.validator.schemas import CUSTOM-SCHEMA
USER_LOGIN_SCHEMA = {
    "username": "",
    "password": ""
}