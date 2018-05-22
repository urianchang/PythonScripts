from flask import request
from prometheus_client import Counter, Histogram
import time
import sys

# <name of metric>, <description>, <list of labels>
REQUEST_COUNT = Counter(
    'request_count', 'App Request Count',
    ['app_name', 'method', 'endpoint', 'http_status']
)

REQUEST_LATENCY = Histogram(
    'request_latency_seconds', 'Request latency',
    ['app_name', 'endpoint']
)

def start_timer():
    request.start_time = time.time()

def stop_timer(response):
    resp_time = time.time() - request.start_time
    # sys.stderr.write("Response time: {}s".format(resp_time))
    REQUEST_LATENCY.labels('test_app', request.path).observe(resp_time)
    return response

def record_request_data(response):
    # sys.stderr.write("Request path: {} Request method: {} Response status: {}".format(request.path, request.method, response.status_code))
    REQUEST_COUNT.labels('test_app', request.method, request.path, response.status_code).inc()
    return response

def setup_metrics(app):
    app.before_request(start_timer)
    # Order matters: stop_timer should be run first
    app.after_request(record_request_data)
    app.after_request(stop_timer)
