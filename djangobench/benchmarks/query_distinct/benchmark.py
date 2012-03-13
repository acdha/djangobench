from benchmark_harness import run_benchmark
from query_distinct.models import Book
from djangobench.utils import do_syncdb


def benchmark():
    list(Book.objects.distinct())

run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta = {
        'description': 'A simple Model.objects.distinct() call.',
    }
)
