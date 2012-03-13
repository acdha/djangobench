from benchmark_harness import run_benchmark
from query_update.models import Book
from djangobench.utils import do_syncdb


def benchmark():
    Book.objects.all().update(title='z')

run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta = {
        'description': 'A simple QuerySet.update().',
    }
)
