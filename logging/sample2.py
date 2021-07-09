import logging

format_str = '%(asctime)s - %(process)d - %(thread)d - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=format_str,level=logging.WARNING)
logger = logging.getLogger(__name__)
logger.debug("debug output")
logger.info("information output")
logger.warning("alerm output")
logger.error("error output")