import sys

from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render_to_response
from django.template  import RequestContext

from benchmark_harness import run_benchmark

from djangobench.utils import do_syncdb


def make_request():
    environ = {
        'PATH_INFO': '/',
        'QUERY_STRING': '',
        'REQUEST_METHOD': 'GET',
        'SCRIPT_NAME': '',
        'SERVER_NAME': 'testserver',
        'SERVER_PORT': 80,
        'SERVER_PROTOCOL': 'HTTP/1.1',
        "wsgi.input": sys.stdin
        }

    return WSGIRequest(environ)


req_object = make_request()


def benchmark():
    render_to_response('list.html',
                       {'numbers': range(0, 200)},
                       context_instance=RequestContext(req_object))

run_benchmark(
    benchmark,
    setup=do_syncdb,
    meta={
        'description': 'Render a l10n intensive template.',
    }
)
