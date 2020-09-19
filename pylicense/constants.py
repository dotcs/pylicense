from typing import List
import logging

DEFAULT_LOGGER_NAME: str = 'pylicense'
LOG_FORMAT: str = logging.BASIC_FORMAT
LOG_LEVELS: List[int] = [logging.ERROR, logging.WARN, logging.INFO, logging.DEBUG]