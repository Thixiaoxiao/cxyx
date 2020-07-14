import logging
from logging.handlers import RotatingFileHandler


class Log:
    def __init__(self, name=__name__,
                 logfile="log.txt",
                 log_to_console=True,
                 log_to_file=False
                 ):
        logger = logging.getLogger(name)
        logger.setLevel(level=logging.INFO)
        logger.handlers.clear()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(process)d - %(thread)d - %(message)s')
        if log_to_file:
            rHandler = RotatingFileHandler(logfile, maxBytes=1 * 1024, backupCount=3)
            rHandler.setLevel(logging.INFO)
            rHandler.setFormatter(formatter)
            logger.addHandler(rHandler)
        if log_to_console:
            console = logging.StreamHandler()
            console.setLevel(logging.INFO)
            console.setFormatter(formatter)
            logger.addHandler(console)
        self.__logger = logger                  

    @property
    def logger(self):
        return self.__logger
