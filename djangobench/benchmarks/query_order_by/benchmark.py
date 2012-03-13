from benchmark_harness import run_benchmark
from query_order_by.models import Book
from djangobench.utils import do_syncdb


def benchmark():
    list(Book.objects.order_by('id'))

run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta = {
        'description': 'A simple Model.objects.order_by() call.',
    }
)
