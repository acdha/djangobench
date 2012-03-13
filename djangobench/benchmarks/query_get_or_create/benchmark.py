import itertools
from benchmark_harness import run_benchmark
from query_get_or_create.models import Book
from djangobench.utils import do_syncdb


counter = itertools.count(1)

def benchmark():
    nextid = counter.next()

    # This will do a create ...
    Book.objects.get_or_create(id=nextid, defaults={'title': 'hi'})

    # ... and this a get.
    Book.objects.get_or_create(id=nextid, defaults={'title': 'hi'})

run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta = {
        'description': 'A Model.objects.get_or_create() call, both for existing and non-existing objects.',
    }
)
