from benchmark_harness import run_benchmark
from query_iterator.models import Book
from djangobench.utils import do_syncdb


def benchmark():
    list(Book.objects.iterator())

run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta = {
        'description': 'A simple Model.objects.iterator() call.',
    }
)
