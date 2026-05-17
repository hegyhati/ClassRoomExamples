# Basic concepts

## Introduction video from last lecture

[MIT | Performance Engineering of Software Systems | Introduction and Matrix Multiplication](https://ocw.mit.edu/courses/6-172-performance-engineering-of-software-systems-fall-2018/resources/lecture-1-intro-and-matrix-multiplication/)

## Performance measurement for backend service

### "Blackbox" / outside testing

Basically: throwing a bunch of requests at the server and measuring:
 - latency
 - throughput
 - failure rate
 - etc.

Note: Average / min / max latency in itself is not too telling -> tail latencies (p50,p90,p95,p99).

Simple tools: 
 - [time + curl](https://curl.se/docs/manpage.html)
 - [hey](https://github.com/rakyll/hey)
 - [wrk](https://github.com/wg/wrk)

The allow simple tests, no "scenarios" or distributed request calls with different endpoints. 
For that, either scripting around these is needed or:
 - [jMeter](https://jmeter.apache.org/)
 - [k6](https://k6.io/)


Typical test types:
 - Stress test - when does it break
 - Ramp up test - how it scales with increased concurrency
 - Endurance test - how it handles traffic in the long term
 - Spike test - how it handles sudden increase in traffic

These are good to "diagnose symptoms", but usually not enough to understand the cause, for that you need:

### Tracing

Basically: "structured logging" what is done, and how long.

Luckily, there is a standard, [Opentelemetry](https://opentelemetry.io/) that is supported by all major languages/tools. 

General idea (simplified):
 - The basic measured block is a span: something that starts and end at some point. For example a DB query, running CPU heavy logic, etc.
 - Anything can be a span, that we consider important enough to measure (manual instrumentation), and many tools add reasonable things by default (automatic instrumentation)
 - spans form a tree 
 - the span with no parent is the root span, and the whole tree is the "trace"

Useful tools for monitoring:
 - [Jaeger](https://www.jaegertracing.io/)
 - [Zipkin](https://zipkin.io/)
 - [Grafana Tempo](https://grafana.com/oss/tempo/)
 - [SigNoz](https://signoz.io/)

Looking at these can answer where the bottlenecks are.
When using a distributed / microservice architecture, tracing can help observability a lot.

**MELT**:
 - Metrics: What is broken?
 - Traces: Where is it broken?
 - Logs: Why is it broken? 


Note: tracing HAS overhead.

## Performance measurement / Profiling of "local stuff"

Flamegraphs are your friends to find out resource (CPU/memory) consumption issues.

Profiling tools fall into 3 categories:

### Samplers
Take a snapshot of the call stack periodically, and guess based on that. Pro: small overhead, Con: approximation.

- **C/C++:** [`perf`](https://perf.wiki.kernel.org/index.php/Main_Page) (Linux kernel sampler)
- **Go:** [`pprof`](https://pkg.go.dev/net/http/pprof) (Built-in runtime sampler)
- **Java:** [Flight Recorder (JFR)](https://docs.oracle.com/javacomponents/jmc-8-jfr-runtime-guide/) (Built-in JVM sampler)
- **C#:** [`dotnet-trace`](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/) (.NET runtime sampler CLI)
- **Rust:** [`flamegraph`](https://github.com/flamegraph-rs/flamegraph) (Cargo plugin wrapping system samplers)

### Instrumentors
Similar to what tracing does, injects hooks. Mostly for interpreted languages. Pro: exact picture, Con: overhead.

- **Python:** [`cProfile`](https://docs.python.org/3/library/profile.html) (Built-in standard profiler)
- **Node.js:** [V8 Profiler & Inspector](https://nodejs.org/en/learn/diagnostics/profiling) (Uses V8 runtime engine hooks)

### Simulators
Basically simulates a virtual machine. Pro: ACCURACY (even cache hits/misses), Con: OVERHEAD (significant). Overkill for managed code.

- **C/C++:** [`Valgrind` (via `callgrind`)](https://valgrind.org/) (The industry-standard simulation framework)

Don't forget to compile with debug symbols (`-g`). 

### Visualization

Bad news, no standard format for profiling data => no standard tool to collect / visualize them. 3 things to note:
 - [Folded stacks / flame graph "standard"](https://www.brendangregg.com/flamegraphs.html)
 - [`pprof` Protobuf](https://github.com/google/pprof/blob/main/proto/profile.proto) - Google binary format adopted by many
 - [Otel Profiling (OMP)](https://github.com/open-telemetry/oteps/blob/main/text/profiles/0128-profile-data-model.md) - hopefully future standard
