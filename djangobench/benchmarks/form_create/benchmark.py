from django import forms
from benchmark_harness import run_benchmark

from djangobench.utils import do_syncdb


class BookForm(forms.Form):
    title = forms.CharField(max_length=100)

def benchmark():
    BookForm({'title': 'a'})

run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta = {
        'description': 'Time required to instantiate and bind a form.',
    }
)
