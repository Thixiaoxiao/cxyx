import time
import traceback
from threading import Thread
try:
    from numba import jit
    from func_timeout import func_set_timeout
except:
    pass
from cxyx.backend import Backend
from cxyx.backend.backend_result import BackendResult
from cxyx.broker import Broker
from cxyx.core.base import TaskBase
from cxyx.core.config import Config
from cxyx.utils.logger import Log


class CXYX:
    def __init__(self, name, broker_info: dict = {}, backend_info=None):
        self.__name = name
        self._init()
        if broker_info:
            self.config_from_object(broker_info)
        if backend_info:
            self.config_from_object(backend_info)

    def _init_broker_backend(self):
        # init broker and backend
        self._broker = Broker()
        self._broker._init()

        self.__backend = Backend()
        self.__backend._init()

    def config_from_object(self, config_dict: dict):
        for key, val in config_dict.items():
            setattr(Config, key.upper(), val)

    def _init(self):
        if not hasattr(self, "_log"):
            self._log = True
            log = Log()
            time.sleep(0.2)
            self.logger = log.logger

    def regist_task(self, func_name, func, kw):
        # 注册任务
        self.logger.info("register task : %s " % func_name)
        task_func_name = "task_" + func_name
        if not hasattr(TaskBase, task_func_name):
            try:
                if "up_speed" in kw and kw["up_speed"]:
                    func = jit()(func)
                if "timeout" in kw and kw["timeout"]:
                    func = func_set_timeout(kw["timeout"])(func)
            except:
                traceback.print_exc()
            setattr(TaskBase, task_func_name, staticmethod(func))
        else:
            self.logger.error(
                "The task : " + func_name + "has exists! Can't register many tasks with one function name!")

    def job(self, function=None, **kw):
        def outer(func):
            def inner(*args, **kwargs):
                result = func(*args, **kwargs)
                return result

            inner.func_name = func.__name__
            self.regist_task(func_name=func.__name__, func=func, kw=kw)
            self.create_task(inner)
            return inner

        if function:
            outer.func_name = function.__name__
            self.create_task(outer)
            return outer(function)
        return outer

    def verb(self, FUNCNAME=None):
        def inner(*args, **kwargs):
            if not hasattr(self, "_broker"):
                self._init_broker_backend()
            # Add task to broker
            _id = self._broker.add_task({
                "func_name": FUNCNAME,
                "args":      args,
                "kwargs":    kwargs
            })
            # return backend obj to get result
            if Config.REDIS_BACKEND:
                return BackendResult(_id=_id, _engine=self.__backend.backend_engine)

        return inner

    def create_task(self, func):
        # add the function : 'verb'
        setattr(func, "verb", self.verb(FUNCNAME=func.func_name))

    def execute_task(self):
        self.logger.info("Worker start to work -------------------------")
        while True:
            task = self._broker.get_task()
            if task:
                res = "error"
                try:
                    self.logger.info("start to consume the task : %s ,parameter : %s -- %s " % (
                        task["func_name"], task["args"], task["kwargs"]))
                    res = getattr(TaskBase, "task_" + task["func_name"])(*task["args"], **task["kwargs"])
                    self.logger.info("success to consume the task : %s ,parameter : %s -- %s " % (
                        task["func_name"], task["args"], task["kwargs"]))
                except:
                    traceback.print_exc()
                    self.logger.error(task["func_name"] + "execute fail!")
                finally:
                    self.logger.info("The task : %s ,parameter : %s -- %s Finished!" % (
                        task["func_name"], task["args"], task["kwargs"]))
                    if getattr(Config, "REDIS_BACKEND"):
                        # Save result to backend
                        self.__backend.save_result(task["id_"], res)
            else:
                time.sleep(1)

    def run(self):
        # Open the worker
        self._init_broker_backend()
        self.execute_task()

    def run_with_many_process(self, count):
        self._init_broker_backend()
        tasks = [
            Thread(target=self.execute_task) for _ in range(count)
        ]
        for task in tasks:
            task.start()
        for task in tasks:
            task.join()
