from benchmark_harness import run_benchmark
from query_select_related.models import Book
from djangobench.utils import do_syncdb


def benchmark():
    for i in xrange(20):
        list(Book.objects.select_related('author'))

run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta = {
        'description': 'A simple Model.objects.select_related() call.',
    }
)
