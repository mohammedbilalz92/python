# region Problem Statement
    # Given an array ‘arr’ of size ‘n’ find the largest element in the array.
    
    # Example:

    # Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]
    # Output: 5

    # Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.
# endregion

from sys import *
from collections import *
from math import *

def largestElement(arr: [], n: int) -> int:

    # assume first element is largest
    largest = arr[0]
    for x in range(1,n): # start from second element
        if arr[x] > largest:
            largest = arr[x]
    return largest


# Test
arr = [1, 2, 3, 4, 5]
n = len(arr)
print(largestElement(arr, n))  # Output: 5

arr2 = [10, 20, 5, 40, 30]
n2 = len(arr2)
print(largestElement(arr2, n2))  # Output: 40