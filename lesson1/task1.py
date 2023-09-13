# написать разбор строки вида “Иванов Иван Иванович 03.10.1997” в 4 поля:
# имя, фамилия, отчество, дата рождения (datetime)
from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    name: str
    sec_name: str
    mid_name: str
    birthday: datetime


def user_info_parser(user_str: str) -> User | None:
    if not isinstance(user_str, str):
        return
    user_list = user_str.split()
    if len(user_list) != 4 or not all(user_list):
        return
    try:
        date = datetime.strptime(user_list[3], "%d.%m.%Y")
    except ValueError:
        return
    return User(name=user_list[1], sec_name=user_list[0], mid_name=user_list[2], birthday=date)


if __name__ == "__main__":
    test_str = "Иванов Иван Иванович 03.10.1997"
    result = user_info_parser(test_str)
    if result:
        print(result)
