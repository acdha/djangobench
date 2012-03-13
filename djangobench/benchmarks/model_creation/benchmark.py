from benchmark_harness import run_benchmark
from model_creation.models import Book

from djangobench.utils import do_syncdb


def benchmark():
    Book.objects.create(title='hi!')

run_benchmark(benchmark, setup=do_syncdb,
              meta={'description': 'Time of a Model.objects.create() call'})