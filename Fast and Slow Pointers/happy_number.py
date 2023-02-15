def is_happy_number(n):
    s = sum_of_digits(n)
    f = sum_of_digits(s)
    while s != f and f != 1:
        s = sum_of_digits(s)
        f = sum_of_digits(sum_of_digits(f))
    return True if f == 1 else False


def sum_of_digits(n):
    suma = 0
    while n > 0:
        digit = n % 10
        suma += digit**2
        n = n // 10
    return suma


n = 23
print(is_happy_number(n))
