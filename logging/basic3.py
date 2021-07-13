import logging

"""
format_str = '%(asctime)s - %(process)d - %(thread)d - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=format_str,level=logging.WARNING)
logger = logging.getLogger(__name__)
logger.debug("debug output")
logger.info("information output")
logger.warning("alerm output")
logger.error("error output")
"""
#logファイルを出力する
std_handler = logging.StreamHandler()
file_handler = logging.FileHandler("tmp.log")

logging.basicConfig(format='%a(sctime)s - %(name)s %(levelname)s -%(message)s',
level=logging.DEBUG, handlers=[std_handler, file_handler])
logger = logging.getLogger(__name__)

logger.debug("デバック出力")
logger.info("情報出力")
logger.warning("警告発生")
logger.error("エラー発生")
