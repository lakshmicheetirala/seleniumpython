import logging
from selenium import webdriver

logging.basicConfig(filename="testlogging.log",format='%(asctime)s: %(levelname)s: %(message)s',level=logging.DEBUG)

logging.debug("This is Debug message")
logging.info("INFO LOg")
logging.warning("Warning")
logging.error("ERROR message")
logging.critical("Critical")