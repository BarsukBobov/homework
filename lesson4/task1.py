# написать функцию для игры в “Угадай число”. В функцию передается число от пользователя и загаданное число. Если
# число равно загаданному вернуть True. Если число больше загаданного вызвать исключение GreaterThen, если меньше -
# LowerThen. при вызове этой функции сделать обработку результатов работы функции. Нет исключения и True - напечатать
# “You win”, GreaterThen - “Your value is greater”, LowerThen - “Your value is lower”

class GreaterThen(Exception):
    pass


class LowerThen(Exception):
    pass


def guess_the_number(number: int, hidden_number: int) -> bool:
    if number == hidden_number:
        return True
    elif number > hidden_number:
        raise GreaterThen()
    else:
        raise LowerThen()


if __name__ == "__main__":
    for numbers in [(2, 2), (3, 2), (2, 3)]:
        try:
            guess_the_number(*numbers)
        except GreaterThen:
            print("Your value is greater")
        except LowerThen:
            print("Your value is lower")
        else:
            print("You win")
