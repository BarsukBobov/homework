l = {"a", 1, 12.0, 1, "b"}
l2 = l
l.update("a")
t1 = ("2", "5")
l.update(t1)
l.remove("b")


l3 = ["a", 1, 12.0, 1, "b"]
s1 = set(l3)

s2 = set(t1)

s3 = set((l3,))
print(s3)

c1 = ("2", "5", 1, 2)
a, b, *c = c1
print(a, b, c)

d1 = {
    1: "a",
    2: "b",
    3: "c"
}

d1[0] = "d"
print(d1)


