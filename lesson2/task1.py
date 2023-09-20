# Реализовать алгоритм поиска простых чисел не более N:
# 1) от 0 до N
# 2) показать N чисел
from typing import List


def get_prime_numbers(n: int) -> List[int]:
    a = [i for i in range(n + 1)]
    lst = []
    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
        for j in range(i, n + 1, i):
            a[j] = 0
        i += 1
    return lst


res = get_prime_numbers(0)
print(res)
