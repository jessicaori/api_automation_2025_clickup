import requests
from utils.logger import Logger

LOGGER = Logger(__name__)

class RestClient:

    def __init__(self):
        self.session = requests.Session()

    def send_request(self, method, url, headers=None, params=None, data=None):
        """
        Sends an HTTP request and returns the response.

        :param method: HTTP method (GET, POST, PUT, DELETE)
        :param url: URL to send the request to
        :param headers: Optional headers for the request
        :param params: Optional query parameters for the request
        :param data: Optional body data for POST/PUT requests
        :return: Response object
        """
        
        response_updated = {}
        methods = {
            'GET': self.session.get,
            'POST': self.session.post,
            'PUT': self.session.put,
            'DELETE': self.session.delete
        }

        try:
            response = methods[method](url=url, headers=headers, params=params, json=data)
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
            response_updated['body'] = response.json() if response.text else { "message": "No content" }
            response_updated['status_code'] = response.status_code
            response_updated['headers'] = dict(response.headers)
            LOGGER.debug('---------------')
            LOGGER.debug(f"Response Body: {response_updated}")
        except requests.exceptions.HTTPError as e:
            LOGGER.error(f"Request failed: %s", e)
        except requests.exceptions.ConnectionError as e:
            LOGGER.error(f"Connection error: %s", e)
        except requests.exceptions.Timeout as e:
            LOGGER.error(f"Request timed out: %s", e)
        except requests.exceptions.RequestException as e:
            LOGGER.error(f"Request Exception: %s", e)

        return response_updated