import argparse
import inspect
import os

# timeit uses either time.time() or time.clock() depending on which is more
# accurate on the current platform:
from timeit import default_timer as time_f

try:
    import cProfile as profile
except ImportError:
    import profile


class SkipBenchmark(Exception):
    pass


benchmark_parser = argparse.ArgumentParser()
benchmark_parser.add_argument('--trials', type=int, default=0)
benchmark_parser.add_argument('--max-time', type=float, default=0.3)


def run_benchmark(benchmark, syncdb=True, setup=None, trials=0, max_time=0, handle_argv=True, meta={}):
    """
    Run a benchmark a few times and report the results.

    Arguments:

        benchmark
            The benchmark callable. ``run_benchmark`` will time
            the executation of this function and report those times
            back to the harness. However, if ``benchmark`` returns
            a value, that result will reported instead of the
            raw timing.

        syncdb
            If True, a syncdb will be performed before running
            the benchmark.

        setup
            A function to be called before running the benchmark
            function(s).

        trials
            The number of times to run the benchmark function. If not given
            and if ``handle_argv`` is ``True`` this'll be automatically
            determined from the ``--trials`` flag.

        handle_argv
            ``True`` if the script should handle ``sys.argv`` and set
            the number of trials accordingly.

        meta
            Key/value pairs to be returned as part of the benchmark results.
    """
    if handle_argv:
        args = benchmark_parser.parse_args()
        trials = trials or args.trials
        max_time = max_time or args.max_time

    print_benchmark_header(benchmark, meta)

    if syncdb:
        from django.core.management import call_command
        call_command("syncdb", verbosity=0)

    if setup:
        setup()

    profile_file = os.environ.get('DJANGOBENCH_PROFILE_FILE', None)

    trial_limited = trials > 0

    while True:
        start = time_f()

        if profile_file is not None:
            loc = locals().copy()
            profile.runctx('benchmark_result = benchmark()', globals(), loc, profile_file)
            benchmark_result = loc['benchmark_result']
        else:
            benchmark_result = benchmark()

        elapsed = benchmark_result or time_f() - start

        print elapsed

        if trial_limited:
            trials -= 1
            if trials < 1:
                break
        else:
            max_time -= elapsed
            if max_time <= 0:
                break


def run_comparison_benchmark(benchmark_a, benchmark_b, syncdb=True, setup=None,
                             trials=None, max_time=None, handle_argv=True, meta={}):
    """
    Benchmark the difference between two functions.

    Arguments are as for ``run_benchmark``, except that this takes 2
    benchmark functions, an A and a B, and reports the difference between
    them.

    For example, you could use this to test the overhead of an ORM query
    versus a raw SQL query -- pass the ORM query as ``benchmark_a`` and the
    raw query as ``benchmark_b`` and this function will report the
    difference in time between them.

    For best results, the A function should be the more expensive one
    (otherwise djangobench will report results like "-1.2x slower", which
    is just confusing).
    """
    if handle_argv:
        args = benchmark_parser.parse_args()
        trials = trials or args.trials
        max_time = max_time or args.max_time

    print_benchmark_header(benchmark_a, meta)

    if syncdb:
        from django.core.management import call_command
        call_command("syncdb", verbosity=0)

    if setup:
        setup()

    trial_limited = trials > 0

    while True:
        start_a = time_f()
        result_a = benchmark_a()
        result_a = result_a or time_f() - start_a

        start_b = time_f()
        result_b = benchmark_b()
        result_b = result_b or time_f() - start_b

        print result_a - result_b

        if trial_limited:
            trials -= 1
            if trials < 1:
                break
        else:
            max_time -= min(result_a, result_b)
            if max_time <= 0:
                break


def print_benchmark_header(benchmark, meta):
    if 'title' not in map(str.lower, meta.keys()):
        meta['title'] = inspect.getmodule(benchmark).__name__
    for key, value in meta.items():
        print '%s: %s' % (key.lower(), value)
    print
