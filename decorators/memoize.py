from collections import defaultdict
from itertools import chain


_memoize_cache = defaultdict(dict)


def memoize(func):
    def wrapper(*args, **kwargs):
        previous_calls = _memoize_cache[func]
        key = str(args) + str({k : kwargs[k] for k in sorted(kwargs)})
        if key in previous_calls:
            return previous_calls[key]
        else:
            result = func(*args, **kwargs)
            previous_calls[key] = result
            return result
    return wrapper


def clear_memoize_cache():
    _memoize_cache.clear()
