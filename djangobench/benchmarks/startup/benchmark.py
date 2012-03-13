# XXX FIXME - has to spawn a new process to measure load time

from benchmark_harness import run_benchmark

def benchmark():
    # Make sure the models and settings are loaded, then we're done. Calling
    # get_models() will make sure settings get loaded.
    from django.db import models
    models.get_models()

run_benchmark(
    benchmark,
    meta = {
        'description': 'Startup time for a simple app.',
    }
)
