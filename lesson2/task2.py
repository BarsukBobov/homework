# Реализовать алгоритм быстрого (бинарного) поиска


def binary_search(num_list: list, number: int) -> int:
    first = 0
    last = len(num_list) - 1

    while first <= last:
        middle = (first + last) // 2
        if number == num_list[middle]:
            return middle
        if number < num_list[middle]:
            last = middle - 1
        else:
            first = middle + 1


test_list = sorted([5, 8, 9, 1, 23, 7, 3, 0, 15])
test_number = 5
print(binary_search(test_list, test_number))
