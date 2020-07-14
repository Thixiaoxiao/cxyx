import logging
from logging.handlers import RotatingFileHandler

from cxyx.core.config import Config


class Log:
    def __init__(self, name=__name__, ):
        logger = logging.getLogger(name)
        logger.setLevel(level=getattr(logging, Config.LOG_LEVEL))
        logger.handlers.clear()
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(process)d - %(thread)d - %(message)s')
        if Config.LOG_TO_FILE:
            rHandler = RotatingFileHandler(Config.LOG_FILE,
                                           maxBytes=Config.LOG_FILE_MAX_BYTES,
                                           backupCount=Config.LOG_FILE_BACKUP_COUNT)
            rHandler.setLevel(getattr(logging, Config.LOG_LEVEL))
            rHandler.setFormatter(formatter)
            logger.addHandler(rHandler)
        if Config.LOG_TO_CONSOLE:
            console = logging.StreamHandler()
            console.setLevel(getattr(logging, Config.LOG_LEVEL))
            console.setFormatter(formatter)
            logger.addHandler(console)
        self.__logger = logger

    @property
    def logger(self):
        return self.__logger
