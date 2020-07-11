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
            print(r"""
                            _ooOoo_
                           o8888888o
                           88" . "88
                           (| -_- |)
                            O\ = /O
                        ____/`---'\____
                      .   ' \\| |// `.
                       / \\||| : |||// \
                     / _||||| -:- |||||- \
                       | | \\\ - /// | |
                     | \_| ''\---/'' | |
                      \ .-\__ `-` ___/-. /
                   ___`. .' /--.--\ `. . __
                ."" '< `.___\_<|>_/___.' >'"".
               | | : `- \`.;`\ _ /`;.`/ - ` : | |
                 \ \ `-. \_ __\ /__ _/ .-` / /
         ======`-.____`-.___\_____/___.-`____.-'======
                            `=---='

         .............................................
                  佛祖镇楼                  BUG辟易
          佛曰:
                  写字楼里写字间，写字间里程序员；
                  程序人员写程序，又拿程序换酒钱。
                  酒醒只在网上坐，酒醉还来网下眠；
                  酒醉酒醒日复日，网上网下年复年。
                  但愿老死电脑间，不愿鞠躬老板前；
                  奔驰宝马贵者趣，公交自行程序员。
                  别人笑我忒疯癫，我笑自己命太贱；
                  不见满街漂亮妹，哪个归得程序员？


Welcome to use CXYX !         
        """)

    @property
    def logger(self):
        return self.__logger
