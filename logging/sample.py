import logging

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
logger.debug("debug output")
logger.info("information output")
logger.warning("alerm output")
logger.error("error output")