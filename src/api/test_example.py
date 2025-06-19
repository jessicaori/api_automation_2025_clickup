from utils.logger import Logger

LOGGER = Logger(__name__)   

class TestExample:
    """Example test class for demonstration purposes."""

    @classmethod
    def setup_class(cls):
        """Set up the test environment."""
        API_KEY = "43009368_f8b8293ed6ca710d1b4384d6ff87fab8f24603a30aa72562d659ea12fe4432c4"
        cls.header_api = {
            "Authorization": f"Bearer {API_KEY}"
        }
        LOGGER.debug("HEADER API: %s", cls.header_api)
        LOGGER.info("Setting up the test environment.")
    
    def setup_method(self):
        """Set up before each test method."""
        LOGGER.info("Setting up before test method.")
        

    def test_one(self):
        """Test case one."""
        LOGGER.info("Running test case one.")

    def test_two(self):
        """Test case two."""
        LOGGER.info("Running test case two.")

    def test_three(self):
        """Test case three."""
        LOGGER.info("Running test case three.")

    def teardown_method(self):
        """Clean up after each test method."""
        LOGGER.info("Tearing down after test method.")

    @classmethod
    def teardown_class(self):
        """Clean up after tests."""
        LOGGER.info("Tearing down the test environment.")
