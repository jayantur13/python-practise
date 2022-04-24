# lambda are anonymous function that can have n arguements but 1 expression

x = lambda a, b: a + b
print(x(2, 5))

y = lambda a: a + 20
print(y(20))


def f1(n):
    return lambda a: a * n


doublethis = f1(2)
print(doublethis(11))

def f2(n):
    return lambda a: a * n


triplethis = f2(3)
print(triplethis(11))

# or use both