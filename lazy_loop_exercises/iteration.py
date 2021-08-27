"""Itertools exercises"""
from itertools import count


def total_length(*args):
    """Return the total number of items in all given iterables."""
    c = count()
    for a in args:
        for item in a:
            next(c)
    return next(c)


def lstrip(iterable,item):
    """Return iterable with strip_value items removed from beginning."""
    first = True
    for i in iterable:
        if i == item and first:
            pass
        else:
            first = False
            yield i
