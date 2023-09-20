# 2. написать разбор строки вида “key1: value1 key2: value2” в словарь


def dict_parser(dict_str: str):
    a = dict_str.split()
    dictionary = {a[i].strip(":"): a[i + 1] for i in range(0, len(a), 2)}
    print(dictionary)


if __name__ == "__main__":
    test_str = "key1: value1 key2: value2 key3: value3"
    dict_parser(test_str)
