"""Iterator exercises"""


def first(iterable):
    """Return the first item in given iterable."""
    iterator = iter(iterable)
    return next(iterator)


def is_iterator(iterable):
    """Return True if given iterable is an iterator."""
    iterator = iter(iterable)
    return iterator is iterable


class Point:
    """3-D Point objects"""

    def __init__(self, x, y, z):
        # self.x = x
        # self.y = y
        # self.z = z
        self.x, self.y, self.z = x, y, z

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __iter__(self):
        # yield self.x
        # yield self.y
        # yield self.z
        yield from (self.x, self.y, self.z)
        # return iter((self.x, self.y, self.z))


def all_same(iterable) -> bool:
    """Return True if all items in the given iterable are the same."""
    f = True
    for current in iterable:
        if f:
            prev = current
            f = False
        if not prev == current:
            return False
        prev = current
    return True


def minmax(iterable):
    """Return minimum and maximum values from given iterable."""
    min, max = None, None
    for i in iterable:
        if (min, max) == (None, None):
            min, max = i, i
            f = False
        if min > i:
            min = i
        if max < i:
            max = i
    if (min, max) == (None, None):
        raise ValueError(f"Empty {iterable} is provided")
    return min, max


from random import randint


class RandomNumberGenerator:
    """Return infinite series of randomly generator numbers."""

    def __init__(self, inital, final):
        self.initial, self.final = inital, final

    def __repr__(self):
        return f"RandomNumberGenerator(initial={self.initial}, final={self.final})"

    def __iter__(self):
        return self

    def __next__(self):
        return randint(self.initial, self.final)
