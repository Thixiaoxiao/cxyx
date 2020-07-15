from cxyx.core.config import Config
from cxyx.utils.redis_engine import RedisEngine
import pickle
import uuid
import sys


class Broker:
    def _init(self):
        if hasattr(Config, "BROKER_INFO"):
            redis_info_dict = getattr(Config, "BROKER_INFO")
            self._broker_engine = RedisEngine(
                redis_host=redis_info_dict[
                    "redis_host"] if "redis_host" in redis_info_dict else Config.REDIS_HOST,
                redis_port=redis_info_dict[
                    "redis_port"] if "redis_port" in redis_info_dict else Config.REDIS_PORT,
                db=redis_info_dict[
                    "redis_db"] if "redis_db" in redis_info_dict else Config.REDIS_DB,
                redis_password=redis_info_dict[
                    "redis_password"] if "redis_password" in redis_info_dict else Config.REDIS_PASSWORD
            )
        elif hasattr(Config, "REDIS_BROKER") and getattr(Config,
                                                         "REDIS_BROKER"):
            self._broker_engine = RedisEngine(
                redis_host=Config.REDIS_HOST,
                redis_port=Config.REDIS_PORT,
                db=Config.REDIS_DB,
                redis_password=Config.REDIS_PASSWORD
            )
        else:
            print("You must set the broker")
            sys.exit(0)

    @property
    def broker_engine(self):
        if not hasattr(self, "_broker_engine"):
            self._init()
        return self._broker_engine

    def add_task(self, task_info):
        task_info["id_"] = str(uuid.uuid1()).replace("-", "")
        self._broker_engine.add_task(Config.BROKER_QUEUE_KEY,
                                     pickle.dumps(task_info))
        return task_info["id_"]

    def get_task(self):
        taskbyte = self._broker_engine.get_task(Config.BROKER_QUEUE_KEY)
        if taskbyte:
            return pickle.loads(taskbyte)
