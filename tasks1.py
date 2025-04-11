def factorial(number: int) -> int:

    if number < 0: raise ValueError

    result = 1

    for element in range(1, number+1):
        result *= element

    return result

def fibonacci(number: int) -> list:

    if number < 0: raise ValueError

    result = [0, 1]
    if number == 0: result = [0]

    for element in range(number):
        fib_number = result[-1] + result[-2]
        result.append(fib_number)

    if number != 0: result.remove(result[-1])

    return result

def count_ones(number: int) -> int:

    if number < 0: raise ValueError
    if not number.is_integer(): raise TypeError

    result = 0

    while number:
        remind = number % 2
        number //= 2

        if remind == 1:
            result += 1

    return result

def is_palindrom(n: int) -> True or False:

    lst_n = []
    result = False

    while n != 0:
        lst_n.append(n % 10)

        n = n // 10

    tls_n = lst_n[:: -1]

    if tls_n == lst_n:
        result = True

    return  result