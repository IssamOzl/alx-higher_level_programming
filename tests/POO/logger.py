#!usr/bin/python3

import logging as log

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

log.basicConfig(filename="./log.Log", level = log.DEBUG, format = LOG_FORMAT)
logger = log.getLogger()

logger.debug("this is debug level message")
logger.info("this is info level message")
logger.warning("this is warning level message")
logger.error("this is error level message")
logger.critical("this is critical level message")

print(logger.level)
