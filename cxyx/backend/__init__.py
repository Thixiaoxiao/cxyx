import pickle

from cxyx.core.config import Config
from cxyx.utils.redis_engine import RedisEngine


class Backend:
    def _init(self):
        if hasattr(Config, "REDIS_BACKEND") and getattr(Config, "REDIS_BACKEND"):
            self._backend_engine = RedisEngine(
                redis_host=Config.REDIS_HOST,
                redis_port=Config.REDIS_PORT,
                db=Config.REDIS_DB,
                redis_password=Config.REDIS_PASSWORD
            )

    @property
    def backend_engine(self):
        if not hasattr(self, "_backend_engine"):
            self._init()
        return self._backend_engine

    def save_result(self, key, val):
        val = pickle.dumps(val)
        self._backend_engine.save_result(key, val, expire_time=Config.RESULT_EXPIRE_TIME)


