"""List comprehension exercises"""


def get_vowel_names(names):
    """Return a list containing all names given that start with a vowel."""
    return [name for name in names if name[0].lower() in ['a', 'e', 'i', 'o', 'u']]


def flatten(matrix):
    """Return a flattened version of the given 2-D matrix (list-of-lists)."""

    return [x
            for data in matrix
            for x in data
            ]


def matrix_from_string(string: str):
    """Convert rows of numbers to list of lists."""
    ret = [[int(i) for i in s.split(" ")] for s in (s for s in string.split("\n"))]
    # strings = [s for s in string.split("\n")]
    # for s in strings:
    #     row = [ int(i) for i in s.split(" ")]
    #     ret.append(row)
    return ret


def power_list(numbers):
    """Return a list that contains each number raised to the i-th power."""
    # ret = []
    # for i in range(0, len(numbers)):
    #     ret.append(numbers[i] ** i)
    # return ret
    # i = 0
    # for number in numbers:
    #     ret.append(number ** i)
    #     i += 1
    # return ret
    from itertools import count
    # return [numbers[i] ** i for i in range(0, len(numbers))]
    c = count(0)
    return [y for number in numbers if (y := number ** next(c)) is not None]


def matrix_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices."""
    # res = []
    # for row1, row2 in zip(matrix1, matrix2):
    #     res_row = []
    #     for col1, col2 in zip(row1, row2):
    #         res_row.append(col1 + col2)
    #     res.append([col1 + col2 for col1, col2 in zip(row1, row2)])
    # return res
    return [[col1 + col2 for col1, col2 in zip(row1, row2)] for row1, row2 in zip(matrix1, matrix2)]


def identity(size: int):
    """Return an identity matrix of size x size."""
    '''[f(x) if condition else g(x) for x in sequence]'''
    # res = []
    # for i in range(0, size):
    #     row = []
    #     for j in range(0, size):
    #         if i == j:
    #             row.append(1)
    #         else:
    #             row.append(0)
    #     res.append([1 if i == j else 0 for j in range(0, size)])
    # return res
    return [[1 if i == j else 0 for j in range(0, size)] for i in range(0, size)]


def triples(num: int):
    """Return list of Pythagorean triples less than input num."""
    t = get_triple(num)
    # return [x for x in t]
    return list(t)


def get_triple(num: int):
    res = []
    for i in range(1, num):
        for j in range(1, num):
            for k in range(1, num):
                if k ** 2 == j ** 2 + i ** 2 and {i, j, k} not in (set(r) for r in res):
                    t = tuple([i, j, k])
                    res.append(t)
                    yield t
