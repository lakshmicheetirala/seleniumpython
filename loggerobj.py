import logging
from selenium import webdriver

logging.basicConfig(filename="testlogging.log",format='%(asctime)s: %(levelname)s: %(message)s',level=logging.DEBUG)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is Debug message")
logger.info("INFO LOg")
logger.warning("Warning")
logger.error("ERROR message")
logger.critical("Critical")