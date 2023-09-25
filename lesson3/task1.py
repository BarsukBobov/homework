# Реализовать абстрактный класс Animal.
# Атрибуты kind: str (собака, кошка и тп), name: str (имя животного).
# Методы voice() -> str,  call(name: str) -> Optional[str].
# Реализовать метод call: если name соответствует имени животного - вернуть результат voice, иначе None.
# Метод voice абстрактный.

# Реализовать 2 потомка Dog, Cat.
# В конструкторах принимать только имя животного, kind передается строкой в родительский конструктор.
# В каждом потомке реализовать метод voice, возвращает транскрипцию издаваемого животным звука.
# Написать скрипт использующий классы Dog и Cat, произвести тестирование классов метода.

from typing import Optional

VOICES = {
    "dog": "bark",
    "cat": "meow"
}


class Animal:
    def __init__(self, kind: str, name: str):
        self.kind = kind
        self.name = name

    def voice(self) -> str:
        pass

    def call(self, name: str) -> Optional[str]:
        if name == self.name:
            return self.voice()


class Dog(Animal):

    def __init__(self, name: str):
        self.name = name
        super().__init__(kind="dog", name=name)

    def voice(self) -> str:
        return VOICES[self.kind]


class Cat(Animal):
    def __init__(self, name: str):
        self.name = name
        super().__init__(kind="cat", name=name)

    def voice(self) -> str:
        return VOICES[self.kind]


if __name__ == "__main__":
    dog = Dog("Barsik")
    cat = Cat("Sharik")
    assert dog.voice() == "bark"
    assert cat.voice() == "meow"
