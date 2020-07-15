import pickle

from cxyx.core.config import Config
from cxyx.utils.redis_engine import RedisEngine


class Backend:
    def _init(self):
        if hasattr(Config, "BACKEND_INFO"):
            redis_info_dict = getattr(Config, "BACKEND_INFO")
            self._backend_engine = RedisEngine(
                redis_host=redis_info_dict[
                    "redis_host"] if "redis_host" in redis_info_dict else Config.REDIS_HOST,
                redis_port=redis_info_dict[
                    "redis_port"] if "redis_port" in redis_info_dict else Config.REDIS_PORT,
                db=redis_info_dict[
                    "redis_db"] if "redis_db" in redis_info_dict else Config.REDIS_DB,
                redis_password=redis_info_dict[
                    "redis_password"] if "redis_password" in redis_info_dict else Config.REDIS_PASSWORD
            )
        elif hasattr(Config, "REDIS_BACKEND") and getattr(Config,
                                                          "REDIS_BACKEND"):
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
        self._backend_engine.save_result(key, val,
                                         expire_time=Config.RESULT_EXPIRE_TIME)
