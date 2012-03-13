from django import template
from benchmark_harness import run_benchmark


def benchmark():
    context = template.Context({
        'stuff': 'something'
    })
    t = template.Template('{{ stuff }}')
    t.render(context)


run_benchmark(
    benchmark,
    meta={
        'description': 'Render an extremely simple template (from string)',
    }
)
