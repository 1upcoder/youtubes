from decorators.memoize import memoize


def test_no_args():
    @memoize
    def unstable():
        from random import randint
        return randint(1, 100)
    assert unstable() == unstable()


def test_some_args():
    @memoize
    def unstable(upper):
        from random import randint
        return randint(1, upper)
    assert unstable(10000) == unstable(10000)
    assert unstable(11000) != unstable(10000)
    assert unstable(11000) == unstable(11000)


def test_some_kwargs():
    @memoize
    def unstable(lower, upper):
        from random import randint
        return randint(lower, upper)
    assert unstable(lower=0, upper=10000) == unstable(lower=0, upper=10000)
    assert unstable(upper=10000, lower=0) == unstable(lower=0, upper=10000)
    assert unstable(lower=0, upper=11000) != unstable(lower=0, upper=10000)
    assert unstable(0, upper=10000) != unstable(lower=0, upper=10000)
