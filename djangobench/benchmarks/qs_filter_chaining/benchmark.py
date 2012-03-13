import datetime
from benchmark_harness import run_benchmark
from qs_filter_chaining.models import Book
from djangobench.utils import do_syncdb


def benchmark():
    Book.objects.filter(title='Talent')\
                .filter(description__icontains='top performers')\
                .filter(author_name__startswith='Geoff')\
                .filter(date_created__lt=datetime.datetime(year=2010, month=1, day=1))\
                .filter(date_created__gte=datetime.date(year=2007, month=1, day=1))\
                .filter(date_published=datetime.datetime.now())\
                .filter(enabled=True)

run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta = {
        'description': 'Filter (but do not execute) a queryset mutliple times.',
    }
)
