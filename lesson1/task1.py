# написать разбор строки вида “Иванов Иван Иванович 03.10.1997” в 4 поля:
# имя, фамилия, отчество, дата рождения (datetime)
from datetime import datetime


def user_info_parser(user_str: str):
    if not isinstance(user_str, str):
        return
    name, sec_name, mid_name, date_str = user_str.split()
    date = datetime.strptime(date_str, "%d.%m.%Y")
    print(name, sec_name, mid_name, date)


if __name__ == "__main__":
    test_str = "Иванов Иван Иванович 03.10.1997"
    user_info_parser(test_str)
