from benchmark_harness import run_benchmark
from query_count.models import Book
from djangobench.utils import do_syncdb


def benchmark():
    Book.objects.count()


run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta = {
        'description': 'A simple Model.objects.count() call.',
    }
)
