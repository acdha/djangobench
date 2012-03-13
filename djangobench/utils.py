from __future__ import absolute_import

from django.core.management import call_command


class SkipBenchmark(Exception):
    pass


def do_syncdb():
    """Simple setup function which runs syncdb for benchmarks"""
    call_command("syncdb", verbosity=0)

