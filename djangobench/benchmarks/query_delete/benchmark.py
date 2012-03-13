import time
from benchmark_harness import run_benchmark
from query_delete.models import Book
from djangobench.utils import do_syncdb


def benchmark():
    b = Book.objects.create(title='hi')
    start = time.time()
    b.delete()
    return time.time() - start

run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta = {
        'description': 'Delete an object via Model.delete().',
    }
)
