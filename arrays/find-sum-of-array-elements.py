# region Problem Statement
    # Given an array 'arr' of size 'n', find the sum of all the elements in the array.  
    # Example:
    # Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]
    # Output: 15
    # Explanation: The sum of the elements in the array {1, 2, 3, 4, 5} is 1 + 2 + 3 + 4 + 5 = 15.
# endregion



from typing import List

def arraySum(arr: List[int], n:int):
    total = 0
    for e in range(n):
        total += arr[e]
    print(total)
    return total


# Test
arr = [1, 2, 3, 4, 5]   
n = len(arr)
print(arraySum(arr, n))  # Output: 15