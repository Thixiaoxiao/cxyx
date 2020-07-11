from cxyx import CXYX

app = CXYX(__name__)
app.config_from_object({
    "redis_host":     ["127.0.0.1"],
    "redis_port":     6379,
    "redis_db":       0,
    "redis_password": "",
    "redis_broker":   True,
    "REDIS_BACKEND":  True
})


@app.job
def add(a, b):
    return a + b


@app.job(k=4)
def muti(a, c):
    return a - c

# @app.job(k=4)
# def muti(a, c):
#     return a - c

# print(dir(Config))
# print(dir(TaskBase))
# print(type(add))
# print(dir(add))
# add.verb(4, 5)
# res = add(4, 5)
# print(res)
# muti.verb(5, 4)
# app.run()
