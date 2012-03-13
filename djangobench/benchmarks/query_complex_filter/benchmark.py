from benchmark_harness import run_benchmark
from query_complex_filter.models import Book
from djangobench.utils import do_syncdb


def benchmark():
    Book.objects.complex_filter({'pk': 1})

run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta = {
        'description': 'A simple Model.objects.complex_filter() call.',
    }
)
