# PROBLEM 13:
# Из Задания 3:
# Составить выражение:
# (a-e**(b/d))%

a = 60
print("a =", a)

b = 12
print("b =", b)

c = 8.12
print("c =", c)

d = 7
print("d =", d)

e = 456
print("e =", e)

print("Наша формула: (a - e ** (b / d)) % c ")

res = (a - e ** (b / d)) % c
print("Результат:", res)