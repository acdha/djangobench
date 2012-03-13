from benchmark_harness import run_benchmark
from query_all_multifield.models import MultiField
from djangobench.utils import do_syncdb


def benchmark():
    list(MultiField.objects.iterator())

def setup():
    do_syncdb()
    for i in range(0, 3000):
        kwargs = {}
        for j in range(1, 11):
            kwargs['field%s' % j] = 'foobar_%s_%s' % (i, j)
        MultiField(**kwargs).save()

run_benchmark(
    benchmark,
    setup=setup,
    meta = {
        'description': 'A simple Model.objects.iterator() call for large number of objects and large number of fields.',
    }
)
