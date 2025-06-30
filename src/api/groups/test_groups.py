import json
import pytest
import allure
from helper.rest_client import RestClient
from helper.validate_response import ValidateResponse
from config.config import base_url, team_id, headers
from utils.logger import Logger
from faker import Faker

LOGGER = Logger(__name__)   

class TestGroups:
    """Test class for Groups API endpoints."""

    @classmethod
    def setup_class(cls):
        """Setup method to initialize class variables."""
        # Arrange
        cls.group_list = []
        cls.rest_client = RestClient()
        cls.validate_response = ValidateResponse()
        cls.faker = Faker()

    @pytest.mark.acceptance
    @pytest.mark.smoke
    @allure.title("Test Create Group")
    @allure.tag('acceptance', 'smoke')
    @allure.label("owner", "jessica.orihuela")
    def test_create_group(self, log_test_name):
        """
        Method to create a group.
        
        Args:
            log_test_name (Fixture): Logs the name of the test being executed.
        """
        LOGGER.info("Creating a group")
        # Body
        body = {
            "name": f"New User Group - {self.faker.company()}"
        }
        # Call Endpoint
        response = self.rest_client.send_request(
            method='POST',
            url=f"{base_url}/team/{team_id}/group",
            headers=headers,
            data=body
        )
        LOGGER.debug("RESPONSE: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("STATUS CODE: %s", response["status_code"])
        self.group_list.append(response["body"]["id"])
        
        # Assertion
        self.validate_response.validate_response(response, "create_group")

    @pytest.mark.acceptance
    @allure.title("Test Get Group")
    @allure.tag('acceptance')
    @allure.label("owner", "jessica.orihuela")
    def test_get_group(self, create_group, log_test_name):
        """
        Method to get a group by ID.
        
        Args:
            create_group (Fixture): Creates a group and returns its ID.
            log_test_name (Fixture): Logs the name of the test being executed.
        """
        LOGGER.info("Getting group with ID: %s")
        # Call Endpoint
        response = self.rest_client.send_request(
            method='GET',
            url=f"{base_url}/group?team_id={team_id}&group_ids={create_group}",
            headers=headers
        )
        LOGGER.debug("RESPONSE: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("STATUS CODE: %s", response["status_code"])
        
        # Assertion
        self.validate_response.validate_response(response, "get_group")
    
    @pytest.mark.acceptance
    @allure.title("Test Update Group")
    @allure.tag('acceptance')
    @allure.label("owner", "jessica.orihuela")
    def test_update_group(self, create_group, log_test_name):
        """
        Method to update a group by ID.
        
        Args:
            create_group (Fixture): Creates a group and returns its ID.
            log_test_name (Fixture): Logs the name of the test being executed.
        """
        LOGGER.info("Updating group with ID with data")
        # Call Endpoint
        response = self.rest_client.send_request(
            method='PUT',
            url=f"{base_url}/group/{create_group}",
            headers=headers,
            data={"name":"Updated Group Name"}
        )
        LOGGER.debug("RESPONSE: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("STATUS CODE: %s", response["status_code"])
        # Assertion
        self.validate_response.validate_response(response, "update_group")

    @pytest.mark.acceptance
    @allure.title("Test Delete Group")
    @allure.tag('acceptance')
    @allure.label("owner", "jessica.orihuela")
    def test_delete_group(self,create_group, log_test_name):
        """
        Method to delete a group by ID.
        
        Args:
            create_group (Fixture): Creates a group and returns its ID.
            log_test_name (Fixture): Logs the name of the test being executed.
        """
        LOGGER.info("Deleting group with ID: %s")
        # Call Endpoint
        response = self.rest_client.send_request(
            method='DELETE',
            url=f"{base_url}/group/{create_group}",
            headers=headers
        )
        LOGGER.debug("RESPONSE: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("STATUS CODE: %s", response["status_code"])
        # Assertion
        self.validate_response.validate_response(response, "delete_group")

    @pytest.mark.functional
    @allure.title("Test Create Group Using Different Data")
    @allure.tag('functional')
    @allure.label("owner", "jessica.orihuela")
    @pytest.mark.parametrize("group_name", ["12121212", "$%&", "<b>Hola</b>"])
    def test_create_group_using_different_data(self, log_test_name, group_name):
        """
        Method to create a group using different data.
        
        Args:
            log_test_name (Fixture): Logs the name of the test being executed.
            group_name (str): The name of the group to be created, can include special characters.
        """
        LOGGER.info("Creating a group")
        # Body
        body = {
            "name": f"{group_name}"
        }
        # Call Endpoint
        response = self.rest_client.send_request(
            method='POST',
            url=f"{base_url}/team/{team_id}/group",
            headers=headers,
            data=body
        )
        LOGGER.debug("RESPONSE: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("STATUS CODE: %s", response["status_code"])
        self.group_list.append(response["body"]["id"])
        
        # Assertion
        self.validate_response.validate_response(response, "create_group")
    
    @pytest.mark.functional
    @allure.title("Test Create a Group without body")
    @allure.tag('functional', 'negative')
    @allure.label("owner", "jessica.orihuela")
    def test_create_group_without_body(self, log_test_name):
        """
        Method to create a group using different data.
        
        Args:
            log_test_name (Fixture): Logs the name of the test being executed.
            group_name (str): The name of the group to be created, can include special characters.
        """
        LOGGER.info("Creating a group")
        # Body
        body = {}
        # Call Endpoint
        response = self.rest_client.send_request(
            method='POST',
            url=f"{base_url}/team/{team_id}/group",
            headers=headers,
            data=body
        )
        LOGGER.debug("RESPONSE: %s", json.dumps(response["body"], indent=4))
        LOGGER.debug("STATUS CODE: %s", response["status_code"])
        self.group_list.append(response["body"]["id"])
        
        # Assertion
        self.validate_response.validate_response(response, "create_group")


    @classmethod
    def teardown_class(cls):
        """Teardown method to clean up after tests."""
        # Cleanup groups created during tests
        LOGGER.info("Test Project Teardown Class")
        for group_id in cls.group_list:
            response = cls.rest_client.send_request(
                method='DELETE',
                url=f"{base_url}/group/{group_id}",
                headers=headers
            )
            # response = requests.delete(url=f"{base_url}/group/{group_id}", headers=headers)
            if response["status_code"] == 200:
                LOGGER.debug("Group deleted")