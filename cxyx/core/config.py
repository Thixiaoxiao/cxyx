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
