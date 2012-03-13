from benchmark_harness import run_benchmark
from query_in_bulk.models import Book
from djangobench.utils import do_syncdb


def benchmark():
    Book.objects.in_bulk([1])

run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta = {
        'description': 'A simple Model.objects.in_bulk() call.',
    }
)
