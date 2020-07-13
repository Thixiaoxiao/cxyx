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
        # 定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
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
        self.welcome()

    def welcome(self):
        if not hasattr(self, "_yt"):
            self._yt = True
            

    @property
    def logger(self):
        return self.__logger
