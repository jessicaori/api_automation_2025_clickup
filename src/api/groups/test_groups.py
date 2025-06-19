import requests
import json
from config.config import base_url, team_id, headers
from utils.logger import Logger

LOGGER = Logger(__name__)   

class TestGroups:
    """Test class for Groups API endpoints."""

    def test_create_group(self, log_test_name):
        """Method to create a group."""
        LOGGER.info("Creating a group")
        # Body
        body = {
            "name": "New User Group name"
        }
        # Call Endpoint
        response = requests.post(url=f"{base_url}/team/{team_id}/group", headers=headers, json=body)
        LOGGER.debug("RESPONSE: %s", response.json())
        assert response.status_code == 200, "Failed to create group"

    def test_get_group(self, create_group, log_test_name):
        """Method to get a group by ID."""
        LOGGER.info("Getting group with ID: %s")
        # Call Endpoint
        response = requests.get(url=f"{base_url}/group?team_id={team_id}&group_ids={create_group}", headers=headers)
        LOGGER.debug("RESPONSE: %s", json.dumps(response.json(), indent=4))
        LOGGER.debug("STATUS CODE: %s", response.status_code)
        assert response.status_code == 200, "Failed to get group"
    
    def test_update_group(self, create_group, log_test_name):
        """Method to update a group by ID."""
        LOGGER.info("Updating group with ID with data")
        response = requests.put(url=f"{base_url}/group/{create_group}", headers=headers, json={"name":"Updated Group Name"})
        LOGGER.debug("RESPONSE: %s", json.dumps(response.json(), indent=4))
        LOGGER.debug("STATUS CODE: %s", response.status_code)
        assert response.status_code == 200, "Failed to update group"

    def test_delete_group(self,create_group, log_test_name):
        """Method to delete a group by ID."""
        LOGGER.info("Deleting group with ID: %s")
        response = requests.delete(url=f"{base_url}/group/{create_group}", headers=headers)
        LOGGER.debug("RESPONSE: %s", json.dumps(response.json(), indent=4))
        LOGGER.debug("STATUS CODE: %s", response.status_code)
        assert response.status_code == 200, "Failed to update group"
