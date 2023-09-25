# Реализовать алгоритм поиска простых чисел не более N:
# 1) от 0 до N
# 2) показать N чисел
from typing import List


def get_prime_numbers(n: int) -> List[int]:
    lst = []
    for i in range(2, n + 1):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


def get_prime_numbers_fixed_count(n: int) -> List[int]:
    lst = []
    i = 2
    while len(lst) < n:
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
        i += 1
    return lst


res = get_prime_numbers(5)
print(res)
res2 = get_prime_numbers_fixed_count(5)
print(res2)
