import logging
from calculator.logger import get_logger

def test_get_logger():
    logger = get_logger("test_logger")
    assert isinstance(logger, logging.Logger)
    assert logger.level in [logging.INFO, 0]  # Default might be 0 (NOTSET)

