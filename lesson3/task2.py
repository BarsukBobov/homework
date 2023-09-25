# Реализовать жадный алгоритм.
# Для последовательности чисел необходимо посчитать подпоследовательности сумма которых равна или более заданного числа.
# Например, дан список [1,10,8, 2] и число 10. результат [[1, 10], [8, 2]]
from typing import List


def greedy_algorithm(lst: List[int], limit: int) -> List[List[int]]:
    lst2 = []
    limit_lst = []
    for elem in lst:
        limit_lst.append(elem)
        if sum(limit_lst) >= limit:
            lst2.append(limit_lst)
            limit_lst = []
    return lst2


if __name__ == "__main__":
    test_lst = [1, 10, 8, 2]
    test_limit = 10
    print(greedy_algorithm(test_lst, test_limit))
