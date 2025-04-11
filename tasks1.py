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
