def factorial(n: int) -> int:
    """
    Calculates the factorial of a positive integer.

    :param n: The integer to calculate the factorial of.
    :return: The factorial of the integer.
    :raises ValueError: If the integer is negative.
    """
    if n < 0:
        raise ValueError(
            'Cannot calculate factorial of a negative number.'
        )
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

        
        
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120

try:
    factorial(-1)
    assert False # pediu 4 asserts
except ValueError:
    pass