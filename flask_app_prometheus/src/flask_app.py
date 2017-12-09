# Python 3.6
from flask import Flask, Response
from helpers.middleware import setup_metrics
import prometheus_client

CONTENT_TYPE_LATEST = str('txt/plain; version=0.0.4; charset=utf-8')

app = Flask(__name__)
setup_metrics(app)

@app.route('/test/')
def test():
    return 'rest'

@app.route('/test1/')
def test1():
    1/0
    return 'rest'

@app.errorhandler(500)
def handle_500(error):
    return str(error), 500

# Exporting Prometheus Metrics
@app.route('/metrics')
def metrics():
    """
    generate_latest returns latest metrics and sets the content type to
    indicate the Prometheus server that we are sending the metrics in text
    format using the 0.0.4 version
    """
    return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == '__main__':
    app.run()
