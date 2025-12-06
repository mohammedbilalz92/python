# region Problem Statement
    # You are given two non-negative integers, ‘NUM1’ and ‘NUM2’, in the form of strings. Return the sum of both strings.

    # Example:
    # Let ‘NUM1’ be: “5”
    # Let ‘NUM2’ be: “21”
    # The sum of both numbers will be: “26”.
# endregion


from os import *
from sys import *
from collections import *
from math import *

def stringSum(num1: str, num2: str) -> str:
    return str(int(num1) + int(num2))


# Test
num1 = "5"
num2 = "21"
print(stringSum(num1, num2))  # Output: "26"
