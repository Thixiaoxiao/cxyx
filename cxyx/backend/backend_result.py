import pickle
import time


class BackendResult:
    def __init__(self, _engine, _id):
        self._id = _id
        self._engine = _engine

    def get_result(self, ):
        time.sleep(0.2)
        res = self._engine.get_result(self._id)

        if res is not None:
            res = pickle.loads(res)
        else:
            res = "result not exist!"
        return res

    def until_get_result(self):
        while True:
            res = self.get_result()
            if res != "result not exist!":
                break
        return res
