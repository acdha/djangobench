from benchmark_harness import run_benchmark
from query_all.models import Book

from djangobench.utils import do_syncdb


def benchmark():
    list(Book.objects.iterator())


def setup():
    do_syncdb()
    for i in range(0, 3000):
        Book(pk=i, title='foobar_%s' % i).save()


run_benchmark(
    benchmark,
    setup=setup,
    meta={
        'description': 'A simple Model.objects.iterator() call for large number of objects.',
    }
)
