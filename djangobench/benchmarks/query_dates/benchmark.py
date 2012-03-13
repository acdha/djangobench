from benchmark_harness import run_benchmark
from query_dates.models import Book
from djangobench.utils import do_syncdb


def benchmark():
    list(Book.objects.dates("created_date", "year", "ASC"))

run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta = {
        'description': 'A simple Model.objects.dates() call.',
    }
)
