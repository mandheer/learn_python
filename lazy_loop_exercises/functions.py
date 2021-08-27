"""Generator Function Exercises."""


def unique(iterable):
    """Yield iterable elements in order, skipping duplicate values."""
    u = set()
    # for i in iterable:
    #     if i not in u:
    #         yield i
    #         u.add(i)
    return (i
            for i in iterable
            if i not in u
            and u.add(i) is None
            )


def float_range(start: float, stop: float, step: float = 1):
    """Return iterable of numbers from start to stop by step."""
    start = start
    while start < stop:
        yield start
        start = start + step


def head(iterable, n: int = 0):
    """Return first n items of a given iterable."""
    for item in iterable:
        if n <= 0:
            break
        n -= 1
        yield item


def pairwise(iterable):
    """
    Yield a tuple containing each item and the item following it.

    The item after the last one is treated as ``None``.
    """
    # if iterable:
    #     i = iter(iterable)
    #     next(i)
    #     for item in iterable:
    #         try:
    #             yield item, next(i)
    #         except StopIteration:
    #             yield item, None

    previous, current = None, None
    for current in iterable:
        if previous:
            yield previous, current
        previous = current
    if previous:
        yield previous, None


def around(iterable):
    """
    Yield a tuple of the previous, current, and next items.

    The previous item should start at ``None`` and the next item should
    be ``None`` for the last item in the iterable.
    """
    previous, current, next_item = None, None, None
    for next_item in iterable:
        if current:
            yield previous, current, next_item
        previous = current
        current = next_item
    if next_item:
        yield previous, current, None


def stop_on(iterable, num: int):
    """Yield from the iterable until the given value is reached."""
    for n in iterable:
        if n == num:
            break
        yield n


def deep_flatten(iterable):
    """Flatten an iterable of iterables."""
    for i in iterable:
        if type(i) is int:
            yield i
        else:
            yield from deep_flatten(i)


def get_primes_over(limit: int = 0):
    """Return given number of primes over 1,000,000."""
    n = 999999
    from generators import is_prime
    while limit > 0:
        if is_prime(n):
            yield n
            limit -= 1
        n += 1
