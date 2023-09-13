# 2. написать разбор строки вида “key1: value1 key2: value2” в словарь


def dict_parser(dict_str: str):
    str_split = [x.strip(":") for x in dict_str.split(" ")]
    quantity = len(str_split)
    if quantity % 2 != 0:
        return
    new_dict = {}
    for i in range(0, quantity, 2):
        new_dict[str_split[i]] = str_split[i + 1]
    print(new_dict)


if __name__ == "__main__":
    test_str = "key1: value1 key2: value2 key3: value3"
    dict_parser(test_str)
