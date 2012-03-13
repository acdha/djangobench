from benchmark_harness import run_benchmark
from query_exclude.models import Book
from djangobench.utils import do_syncdb


def benchmark():
    list(Book.objects.exclude(id=1))

run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta = {
        'description': 'A simple Model.objects.exclude() call.',
    }
)
