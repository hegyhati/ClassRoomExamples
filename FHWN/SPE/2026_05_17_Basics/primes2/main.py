from flask import Flask, json, jsonify

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

# 1. Setup the Resource and Provider
resource = Resource.create({"service.name": "primes2"})
provider = TracerProvider(resource=resource)

# 2. Configure the OTLP Exporter (gRPC default on port 4317)
processor = BatchSpanProcessor(
    OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
)
provider.add_span_processor(processor)

# 3. Set the global tracer provider FIRST
trace.set_tracer_provider(provider)

# 4. Get manual tracer
tracer = trace.get_tracer(__name__)

app = Flask(__name__)

# 5. Instrument the Flask app 
FlaskInstrumentor().instrument_app(app)


def is_prime(num: int) -> bool:
    with tracer.start_as_current_span("is_prime"):
        if num < 2: return False
        for div in range(2, num):
            if num % div == 0:
                return False
        return True


def primes_in_range(start: int, end: int | None = None) -> list[int]:
    if end is None: end = 2 * start
    with tracer.start_as_current_span("primes_in_range"):
        return [num for num in range(start, end) if is_prime(num)]


@app.route("/primes/<int:num>")
def primes_in_range_1(num: int):
    return jsonify(primes_in_range(num))


@app.route("/primes/<int:num>/<int:num2>")
def primes_in_range_2(num: int, num2: int):
    return jsonify(primes_in_range(num, num2))


CACHE_FILE = "primes.json"

def primes_in_range_cached(start: int, end: int | None = None) -> list[int]:
    with tracer.start_as_current_span("load_cache"):
        with open(CACHE_FILE) as f:
            cached_primes = json.load(f)
    with tracer.start_as_current_span("prima_range_cached"):
        primes = []
        for num in range(start, end):
            if num in cached_primes:
                primes.append(num)
            elif is_prime(num):
                primes.append(num)
                cached_primes.append(num)
    with tracer.start_as_current_span("save_cache"):
        with open(CACHE_FILE, "w") as f:
            json.dump(cached_primes, f)
    return primes
    
@app.route("/primes/cached/<int:num>/<int:num2>")
def primes_in_range_cached_2(num: int, num2: int):
    return jsonify(primes_in_range_cached(num, num2))

if __name__ == "__main__":
    app.run(debug=True)