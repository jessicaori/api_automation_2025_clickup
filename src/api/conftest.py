import json
import pytest
import requests
from config.config import base_url, team_id, headers
from utils.logger import Logger

LOGGER = Logger(__name__)   

@pytest.fixture
def log_test_name(request):
    """Fixture to log the name of the test being executed."""
    test_name = request.node.name
    LOGGER.info(f" ==> STARTING TEST: '{test_name}'")
    yield
    LOGGER.info(f" ==> FINISHED TEST: '{test_name}'")

@pytest.fixture
def create_group():
    """Fixture to create a group."""
    # Body
    body = {
        "name": "New User Group name - from Test"
    }
    # Call Endpoint
    response = requests.post(url=f"{base_url}/team/{team_id}/group", headers=headers, json=body)
    LOGGER.debug("RESPONSE: %s", response.json())
    group_id=response.json().get('id')
    yield group_id
    delete_group(group_id)

def delete_group(group_id):
    """Fixture to delete a group."""
    LOGGER.info("Deleting group with ID: %s")
    response = requests.delete(url=f"{base_url}/group/{group_id}", headers=headers)
    # LOGGER.debug("RESPONSE: %s", json.dumps(response.json(), indent=4))
    LOGGER.debug("STATUS CODE: %s", response.status_code)
