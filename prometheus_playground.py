# Python 2.7
from prometheus_client import start_http_server, Summary
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(6767)
    # Generate some requests.
    while True:
        # pass
        process_request(random.random())

"""
* request_processing_seconds_count: Number of times this function was called
* request_processing_seconds_sum: Total amount of time spent in this function

What's shown in HTML:

# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="2",minor="7",patchlevel="13",version="2.7.13"} 1.0
# HELP request_processing_seconds Time spent processing request
# TYPE request_processing_seconds summary
request_processing_seconds_count 121.0
request_processing_seconds_sum 57.97495794296265
"""
