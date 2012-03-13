from benchmark_harness import run_benchmark
from query_values_list.models import Book
from djangobench.utils import do_syncdb


def benchmark():
    list(Book.objects.values_list('title'))


run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta={
        'description': 'A simple Model.objects.values_list() call.',
    }
)
