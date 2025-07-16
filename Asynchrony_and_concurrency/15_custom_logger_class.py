import logging
from typing import Optional


class CustomLogger:
    """
    A custom logger wrapper for Python's logging module to provide
    consistent and reusable logging setup across applications.
    """

    def __init__(
        self,
        name: str,
        level: int = logging.INFO,
        log_to_file: bool = False,
        file_path: Optional[str] = None,
        log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        date_format: str = "%Y-%m-%d %H:%M:%S",
    ):
        """
        Initialize the custom logger.

        Args:
            name (str): The logger name.
            level (int): The logging level (e.g., logging.INFO, logging.DEBUG).
            log_to_file (bool): Whether to log to a file.
            file_path (str): Path to the log file if log_to_file is True.
            log_format (str): Format for log messages.
            date_format (str): Format for timestamps in log messages.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Prevent adding handlers multiple times
        if not self.logger.handlers:
            formatter = logging.Formatter(log_format, datefmt=date_format)

            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

            # Optional file handler
            if log_to_file and file_path:
                file_handler = logging.FileHandler(file_path)
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        """
        Retrieve the configured logger instance.

        Returns:
            logging.Logger: Configured logger.
        """
        return self.logger


# Example usage
def main():
    """
    Demonstrate the usage of CustomLogger.
    """
    logger = CustomLogger(
        "MyCustomLogger", level=logging.ERROR
    ).get_logger()  # you can change the level to DEBUG, INFO, etc.

    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning.")
    logger.error("This is an error.")
    logger.critical("This is a critical error.")


if __name__ == "__main__":
    main()
# This code defines a custom logger class that can be used to create a logger with specific configurations.
# It allows logging to both console and file, with customizable formats and levels.
