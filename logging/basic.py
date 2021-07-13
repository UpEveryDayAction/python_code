import logging

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)
logger.debug("debug output")
logger.info("information output")
logger.warning("alerm output")
logger.error("error output")
logger.critical("yabai")