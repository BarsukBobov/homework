# l = ["a", "b", "c"]
# if "a" in l:
#     print(True)


# def a(_dict, num):
#     for d in _dict:
#         if d > num:
#             return _dict[d]
#
#
# d = {
#     1: 1,
#     2: "val"
# }
# print(a(d, 2))
# n = 0
# while True:
#     if n == 20:
#         break
#     n += 1
#     if n % 2 == 0:
#         continue
#     print(n)

# _str = "Кирилл"
# print("Привет, {}".format(_str) if _str == "Кирилл" else "Привет")
# with open("1.txt", "r") as f:
#     f.read()

# множественное наследование
class A:
    def __init__(self, a):
        self.a = a

    def b(self):
        print("A")


class B:
    def b(self):
        print("B")


class D:
    def b(self):
        print("D")


class C(A, B, D):
    def __init__(self, b, a):
        super().__init__(a)
        self.b = b

    def b(self):
        print("C")


c = C(a=2, b=1)
print(c.__dict__)
print(c)