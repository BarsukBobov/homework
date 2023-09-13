# 2. написать разбор строки вида “key1: value1 key2: value2” в словарь
import re


def dict_parser(dict_str: str) -> dict | None:
    if not isinstance(dict_str, str):
        return
    match_result = re.findall(r"(\w+): *(\w+)", dict_str)
    if not match_result:
        return
    new_dict = {}
    for match in match_result:
        new_dict.__setitem__(*match)
    return new_dict


if __name__ == "__main__":
    test_str = "key1: value1 key2: value2 key3: value3"
    result = dict_parser(test_str)
    if result:
        print(result)
