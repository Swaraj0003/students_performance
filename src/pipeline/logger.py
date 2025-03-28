import logging

# Configure logging
logging.basicConfig(
    filename="app.log",  # Log file name
    level=logging.DEBUG,  # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    filemode="a"  # Append mode (use "w" to overwrite)
)

# Create a logger instance
logger = logging.getLogger(__name__)
