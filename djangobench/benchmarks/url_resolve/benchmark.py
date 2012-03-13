from django.core.urlresolvers import resolve
from benchmark_harness import run_benchmark

def benchmark():
    resolve('/basic/')
    resolve('/fallthroughview/')
    resolve('/replace/1')

run_benchmark(
    benchmark,
    meta = {
        'description': 'URL resolution.',
    }
)
