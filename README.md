Cxyx
=======

*Installation*
------------

​        $ pip install cxyx

## *Example*

##### Create task.py and edit：

```Python
from cxyx import CXYX

app = CXYX(__name__)
app.config_from_object({
    "redis_host": ["127.0.0.1"],
    "redis_port": 8090,
    "redis_password": "",
    "redis_broker": True,
    "redis_backend": True
})


@app.job()
def muti(a, b):
    return a - b


@app.job
def add(a, b):
    return a + b
```

##### Create produce.py and Edit:

```Python
from task import add, muti

add.verb(4, 5)  # Add task async.

res_obj = muti.verb(4, 5)
result = res_obj.until_get_result() # Block until get the result.
```

Start the consumers in cmd:

`cxyx worker task:app`

##  *Illustration*

​        It‘s used in a way similar to Celery. However, because Celery cannot use redis cluster, so I developed this framework, and open source it. If you need to use redis cluster, you can consider my framework . If not, it is recommended that you use Celery because it is powerful.  Of course, I will continue to maintain my framework. You are welcome to join the maintenance.   
