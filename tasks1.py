def factorial(number: int) -> int:

    if number < 0: raise ValueError

    result = 1

    for element in range(1, number+1):
        result *= element

    return result
