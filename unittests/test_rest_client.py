import unittest
import json
from utils.logger import Logger
from helper.rest_client import RestClient
from config.config import base_url, team_id, headers

LOGGER = Logger(__name__)

class TestRestClient(unittest.TestCase):

    def test_get_rest_client(self):
        """Test the RestClient"""
        LOGGER.info("Testing RestClient")
        rest_client = RestClient()
        response = rest_client.send_request(
            method='GET',
            url=f"{base_url}group?team_id={team_id}",
            headers=headers
        )
        LOGGER.debug(json.dumps(response, indent=4))
    
    def test_get_rest_client_negative(self):
        """Test the RestClient with an invalid URL"""
        LOGGER.info("Testing RestClient with an invalid URL")
        rest_client = RestClient()
        response = rest_client.send_request(
            method='GET',
            url=f"{base_url}group?team_id={team_id}sdfsd",
            headers=headers
        )
        LOGGER.debug(json.dumps(response, indent=4))
    
    def test_post_rest_client_create_project_without_body_negative(self):
        """Test the RestClient with an invalid POST request"""
        LOGGER.info("Testing RestClient with an invalid POST request")
        rest_client = RestClient()
        response = rest_client.send_request(
            method='POST',
            url=f"{base_url}/team/{team_id}/group",
            headers=headers # With missing body data
        )
        LOGGER.debug(json.dumps(response, indent=4))
        