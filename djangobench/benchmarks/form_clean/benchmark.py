from django import forms
from benchmark_harness import run_benchmark
from djangobench.utils import do_syncdb


class BookForm(forms.Form):
    title = forms.CharField(max_length=100)

form = BookForm({'title': 'hi'})

run_benchmark(
    form.full_clean,
    setup=do_syncdb,
    meta={
    'description': 'Speed of a Form.clean call.',
    }
)
