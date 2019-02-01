from celery import Celery

# 'tasks': name of the current module so name can be automatically generated in __main__ module
# 'broker': URL of the message broker that you want to use
app = Celery(
    'tasks',
    backend='rpc://',
    broker='pyamqp://guest@localhost//',
)

# 'amqp' - RabbitMQ  |  'redis' - Redis
# Make sure RabbitMQ-Server is running before running the script

@app.task
def add(x, y):
    return x + y
