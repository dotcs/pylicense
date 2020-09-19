import logging
import sys

import pylicense.constants as pc

def configure_logger() -> logging.Logger:
    logger = logging.getLogger(pc.DEFAULT_LOGGER_NAME)
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(pc.LOG_FORMAT)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger