# Celery Notes

Three core components:

1. Celery client: Used to issue background jobs
2. Celery workers: Processes that run the background jobs
3. Message broker: Client communicates with the workers through
a message queue.

Popular message broker choices:

* RabbitMQ
    - Start the server: `sudo rabbitmq-server` (add `-detached` to run in
    the background.)
    - Stop the server: `sudo rabbitmqctl stop`
* Redis
    - More susceptible to data loss in the event of abrupt termination or
    power failures.

Example of running Celery worker server:

```
celery -A tasks worker --loglevel=info
```

## Calling a task and keeping results

To call a task, use the `delay()` method, which returns an `AsyncResult` instance.
This can be used to check the state of the task, wait for the task to finish,
or get its return value (or if the task failed, to get the exception and
traceback).

Results are not enabled by default. In order to do remote procedure calls or
keep track of task results in a database, Celery will need to be configured
to use a result backend.

`ready()` method returns whether the task has finished processing or not.

**WARNING**
Backends use resources to store and transmit results. To ensure that resources
are released, you must eventually call `get()` or `forget()` on EVERY `AsyncResult`
instance returned after calling a task.


## Configuration

Celery input is connected to a broker and the output can be optionally connected
to a result backend.

Configuration can be set on the app directly or by using a dedicated configuration
module (e.g. `celeryconfig.py`). To tell Celery instance to use a configuration
module, call `app.config_from_object()` method.

Refer to [Configuration and defaults](http://docs.celeryproject.org/en/latest/userguide/configuration.html#configuration) for more information.
