class Config:
    # USE Redis
    REDIS_DB = 0
    REDIS_HOST = ["127.0.0.1"]
    REDIS_PASSWORD = ""
    REDIS_PORT = 6379

    BROKER_QUEUE_KEY = "CXYX-task-list"

    # If use redis as broker , choose True
    REDIS_BROKER = False

    # The time of result save in backend
    RESULT_EXPIRE_TIME = 60 * 60 * 24 * 2

    # If use redis as backend , choose True
    REDIS_BACKEND = False

    # log
    LOG_FILE = "CXYX"
    LOG_LEVEL = "INFO"
    # Log printing to terminal
    LOG_TO_CONSOLE = True
    # Log saved to file
    LOG_TO_FILE = False
    LOG_FORMATTER_STR = '%(asctime)s - %(levelname)s - %(process)d - %(thread)d - %(message)s'
    # Maximum size of log file
    LOG_FILE_MAX_BYTES = 1024 * 1024 * 3
    # Maximum number of log files
    LOG_FILE_BACKUP_COUNT = 3
