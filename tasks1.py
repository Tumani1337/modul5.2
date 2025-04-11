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
    if not isinstance(n, int): raise TypeError
    lst_n = []
    result = False
    if n < 0:
        return False
    while n != 0:
        lst_n.append(n % 10)

        n = n // 10

    tls_n = lst_n[:: -1]

    if tls_n == lst_n:
        result = True

    return  result

def gcd(number1: int, number2: int) -> int:

    if number1 < 0: raise ValueError
    if number2 < 0: raise ValueError
    if not number1.is_integer(): raise TypeError
    if not number2.is_integer(): raise TypeError

    result = [min(number1, number2), max(number1, number2)]
    result1 = [result[0], result[1]]

    while result1[0] != result1[1] and result1[1] != 0:

        result1[0], result1[1] = min(result), max(result)
        result = result1

        result[1] = result[1] % result[0]

    return result1[0]