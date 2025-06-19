"""This module defines a custom logger class that extends the standard Python logging.Logger.
It allows logging to both the console and a file with a custom format."""
import logging


class Logger(logging.Logger):
    """Class to manage a custom logger
    """

    def __init__(self, name):
        """Initializes the logger"""
        super().__init__(name)
        self.configure()

    def configure(self):
        """Configures handlers, levels and formatters"""

        # Create handlers
        console_handler = logging.StreamHandler()  # Logs to console
        file_handler = logging.FileHandler('file.log')  # Logs to file

        # Set levels
        console_handler.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.DEBUG)

        # Create a formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Attach formatter to handlers
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Attach handlers to logger
        self.addHandler(console_handler)
        self.addHandler(file_handler)


    def close(self):
        """Method to close and flush all the handlers"""
        for handler in self.handlers:
            handler.flush()
            handler.close()
