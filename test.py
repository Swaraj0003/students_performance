import logging

# Configure logging to save only WARNING and above
logging.basicConfig(
    filename="app.log",
    level=logging.WARNING,  # Only WARNING, ERROR, CRITICAL will be logged
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"  # Append logs instead of overwriting
)

# Logging various messages
logging.debug("This is a debug message")  # Won't be logged
logging.info("This is an info message")  # Won't be logged
logging.warning("This is a warning message")  # Logged
logging.error("This is an error message")  # Logged
logging.critical("This is a critical message")  # Logged

print("Check 'app.log' - INFO is not logged, only WARNING and above are.")
