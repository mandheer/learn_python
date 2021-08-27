# ============================================
# numbers = [1, 2, 3, 5, 7]
# for number in numbers:
#     print(number)

# my_fav_numbers = [2, 1, 3, 4, 7, 11, 18]
# doubled_numbers = []
# for n in my_fav_numbers:
#     doubled_numbers.append(n*2)

# doubled_numbers = (n * 2
#                    for n in my_fav_numbers
#                    )
#
#
# def get_double(numbers):
#     for n in numbers:
#         yield n * 2
#
#
# double_num = get_double(my_fav_numbers)
# print(next(double_num))
# print([n for n in double_num])
# ====================================================
# def count(n: int = 0):
#     print("start")
#     while True:
#         yield n
#         n += 1
#         print("loop")
#     print("end")
#
#
# c = count()
#
# for x in c:
#     print(x)
#     if x > 3:
#         break
# ====================================================
# import sys
# def is_prime(candidate: int) -> bool:
#     for n in range(2, candidate // 2):
#         if candidate % n == 0:
#             return False
#     return True
#
#
# def get_big_primes(occurrences: int = 1):
#     print("start")
#     n = 999999
#     count = 0
#     while count < occurrences:
#         if is_prime(n):
#             print(f"Found prime {n}")
#             yield n
#             count += 1
#         n += 1
#     print("end")
#
#
# limit = int(sys.argv[1])
#
# for prime in get_big_primes(occurrences=limit):
#     print(prime)
# ===========================================
# Python 3 syntax for yield
# def generatorify(iterable):
#     yield from iterable
#
# def generatorify(iterable):
#     for x in iterable:
#         yield x
# ============================================
#
# def trim_line_endings(lines):
#     for line in lines:
#         yield line.rstrip("\n")
#
# def trim_line_endings(lines):
#     return (
#         line.rstrip("\n")
#         for line in lines
#     )
# lines = ["hello \n","there \n"]
# print(list(trim_line_endings(lines)))
# ============================================
#
# def print_each(iterable):
#     for item in iterable:
#         print(item)
#
#
# def print_each(iterable):
#     iterator = iter(iterable)
#     while True:
#         try:
#             item = next(iterator)
#         except StopIteration:
#             break
#         else:
#             print(item)
#
#
# print_each([1, 2, 3])
# print_each(['a', 'b', 'c'])
# ======================================

dict = {}
iter