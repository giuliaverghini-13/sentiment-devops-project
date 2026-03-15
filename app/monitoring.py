# Monitoring logic for sentiment analysis app
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

# Total number of prediction requests
REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total number of prediction requests"
)

# Total number of prediction errors
PREDICTION_ERRORS = Counter(
    "prediction_errors_total",
    "Total number of prediction errors"
)

# Time spent handling prediction requests
PREDICTION_LATENCY = Histogram(
    "prediction_latency_seconds",
    "Time spent processing prediction requests"
)
from prometheus_client import Gauge
import psutil

# CPU usage
CPU_USAGE = Gauge(
    "cpu_usage_percent",
    "CPU usage percentage"
)

# Memory usage
MEMORY_USAGE = Gauge(
    "memory_usage_percent",
    "Memory usage percentage"
)


def update_system_metrics():
    CPU_USAGE.set(psutil.cpu_percent())
    MEMORY_USAGE.set(psutil.virtual_memory().percent)