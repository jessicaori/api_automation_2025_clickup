import unittest
from utils.logger import Logger

LOGGER = Logger(__name__)   

class TestLogger(unittest.TestCase):
    def test_logger(self):
        LOGGER.debug("This is a debug message")
        LOGGER.info("This is an info message")
        LOGGER.warning("This is a warning message")
        LOGGER.error("This is an error message")
        LOGGER.critical("This is a critical message")