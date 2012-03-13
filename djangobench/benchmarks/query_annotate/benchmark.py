from django.db.models import Count
from benchmark_harness import run_benchmark
from query_annotate.models import Book
from djangobench.utils import do_syncdb


def benchmark():
    list(Book.objects.values('title').annotate(books_total=Count('id')))

run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta = {
        'description': 'A simple Model.objects.annotate() call.',
    }
)
