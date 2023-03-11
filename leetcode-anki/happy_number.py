def isHappy(n):
    s = getSum(n)
    f = getSum(getSum(s))
    while s != f and f != 1:
        s = getSum(s)
        f = getSum(getSum(f))
    return True if f == 1 else False


def getSum(n):
    suma = 0
    while n > 0:
        suma += (n % 10) ** 2
        n = n // 10
        print(suma)
    return suma


def isHappy2(n):
    s = getSum2(n)
    f = getSum2(getSum2(s))
    while s != f and f != 1:
        s = getSum2(s)
        f = getSum2(getSum2(f))
    return True if f == 1 else False


def getSum2(nr):
    suma = 0
    while nr:
        suma += (nr % 10) ** 2
        nr = nr // 10
    return suma


n = 19
print(isHappy2(n))
