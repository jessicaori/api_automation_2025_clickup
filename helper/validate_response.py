import json
import jsonschema
from utils.logger import Logger

LOGGER = Logger(__name__)

class ValidateResponse:
    """
    Class to validate API responses.
    """

    def validate_response(self, actual_response, file_name):
        expected_response = self.read_input_data(f"src/api/input_json/{file_name}.json")
        self.validate_value(actual_response['body'], expected_response["body"], 'body')
        self.validate_value(actual_response['status_code'], expected_response["status_code"], 'status_code')
        self.validate_value(actual_response['headers'], expected_response["headers"], 'headers')

    def validate_value(self, actual_value, expected_value, key_compare):
        if key_compare == 'status_code':
            assert actual_value == expected_value, f"Expected status code {expected_value}, but got {actual_value}"
        elif key_compare == 'headers':
            LOGGER.debug(f"Expected headers: {json.dumps(expected_value, indent=4)}")
            LOGGER.debug(f"Actual headers: {json.dumps(actual_value, indent=4)}")
            assert expected_value.keys() <= actual_value.keys(), f"Expected headers {expected_value}, but got {actual_value}"
        elif key_compare == 'body':
            schema = False
            try: 
                jsonschema.validate(instance=actual_value, schema=expected_value)
                LOGGER.debug("JSON Schema Validation Successful")
                schema = True
            except jsonschema.exceptions.ValidationError as e:
                LOGGER.error("JSON Schema Validation Error: %s", e)
                raise e
            assert schema, f"Expected body {expected_value}, but got {actual_value}"

    def read_input_data(self, file_name):
        LOGGER.debug("Reading input data from file: %s", file_name)
        with open(file_name, encoding="utf-8") as f:
            data = json.load(f)
        LOGGER.debug("Content data: %s", data)
        return data
