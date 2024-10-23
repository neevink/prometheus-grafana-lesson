import time
import threading
import random

from flask import Flask
from prometheus_client import Counter, Gauge, Histogram, start_http_server

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'status_code'])
IN_PROGRESS = Gauge('app_inprogress_requests', 'Number of in-progress requests')
LATENCY = Histogram('app_request_latency_seconds', 'Latency of HTTP Requests', ['method', 'endpoint'])


@app.route('/process')
def process():
    start_time = time.time()

    with IN_PROGRESS.track_inprogress():
        delay = random.uniform(0.01, 0.2)
        time.sleep(delay)

        # Делаем вид, что действительно выполняем полезную работу

        status_codes = [200, 404, 400, 500]
        status_code = random.choice(status_codes)

        REQUEST_COUNT.labels(method='GET', endpoint='/process', status_code=status_code).inc()

    latency = time.time() - start_time
    LATENCY.labels(method='GET', endpoint='/process').observe(latency)

    return "Processed!\n", status_code


def start_metrics_server():
    start_http_server(8000)


if __name__ == '__main__':
    metrics_thread = threading.Thread(target=start_metrics_server)
    metrics_thread.start()

    app.run(host='0.0.0.0', port=5000)
