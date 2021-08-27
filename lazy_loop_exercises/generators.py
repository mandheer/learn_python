"""Generator Expression Exercises."""


def sum_all(matrix):
    """Return the sum of all numbers in the given list-of-lists."""
    # total: int = 0
    # for number in matrix:
    #     total += sum(number)
    return sum(n for number in matrix for n in number)


def all_together(*arg, **kwargs):
    """String together all items from the given iterables."""
    # for data in arg:
    #     for a in data:
    #         yield a
    return (a for data in arg for a in data)


def interleave(iterable1, iterable2):
    """Return iterable of one item at a time from each list."""
    for i1, i2 in zip(iterable1, iterable2):
        yield i1
        yield i2


def deep_add(iterable1):
    """Return sum of values in given iterable, iterating deeply."""
    total: int = 0
    try:
        for x in iterable1:
            total += deep_add(x)
    except TypeError:
        total += iterable1
    return total


def parse_ranges(number_range: str):
    """Return a list of numbers corresponding to number ranges in a string"""
    ret = []
    pairs = (
        group.split('-')
        for group in number_range.split(',')
    )

    # for start, end in pairs:
    #     for d in range(int(start), int(end) + 1):
    #         ret.append(d)
    return [
        d
        for start, end in pairs
        for d in range(int(start), int(end) + 1)
    ]


def is_prime(candidate: int):
    """Return True if candidate number is prime."""
    # for n in range(2, candidate // 2):
    #     if candidate % n == 0:
    #         return False
    # return True
    return not any(candidate % n == 0 for n in range(2, candidate // 2))
