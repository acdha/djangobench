from django.db.models import Count
from benchmark_harness import run_benchmark
from query_aggregate.models import Book

from djangobench.utils import do_syncdb


def benchmark():
    Book.objects.all().aggregate(Count('title'))

run_benchmark(benchmark, setup=do_syncdb,
              meta={'description': 'A simple Model.objects.aggregate() call.'})
