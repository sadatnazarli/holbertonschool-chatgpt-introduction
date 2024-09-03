#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Function Description:
    This function recursively calculates the factorial of a given non-negative integer `n`.
    The factorial of `n` is the product of all positive integers less than or equal to `n`.
    By definition, the factorial of 0 is 1.

    Parameters:
    n (int): A non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the input number `n`.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Retrieve the integer from command-line arguments, calculate the factorial, and print it
f = factorial(int(sys.argv[1]))
print(f)

