from redis import StrictRedis, ConnectionPool
from rediscluster import StrictRedisCluster


class RedisEngine:
    @property
    def engine(self):
        return self.redis_eng

    def __init__(self, redis_host, redis_port, redis_password, db=0):
        if isinstance(redis_host, list) and len(redis_host) == 1:
            redis_host = redis_host[0]
        if isinstance(redis_host, str):
            conn_pool = ConnectionPool(
                host=redis_host,
                port=redis_port,
                db=db,
                password=redis_password
            )
            self.redis_eng = StrictRedis(connection_pool=conn_pool, max_connections=10, )
        elif isinstance(redis_host, list):
            self.redis_eng = StrictRedisCluster(startup_nodes=[
                {"host": host, "port": redis_port, "password": redis_password} for host in redis_host
            ])

    def lpush(self, key, val):
        self.redis_eng.lpush(key, val)

    def lpop(self, key):
        return self.redis_eng.lpop(key)

    def rpush(self, key, val):
        self.redis_eng.rpush(key, val)

    def rpop(self, key):
        return self.redis_eng.rpop(key)

    def add_task(self, key, val, **kwargs):
        self.redis_eng.lpush(key, val)

    def get_task(self, key):
        return self.rpop(key)

    def save_result(self, key, val, expire_time):
        res = self.redis_eng.set(key, val, nx=False, px=expire_time)
        if not res:
            print("id : %s has exists!" % key)

    def get_result(self, key):
        res = self.redis_eng.get(key)
        if res is not None:
            self.redis_eng.delete(key)
        return res
