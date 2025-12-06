# region Problem Statement

    # You are given an array ‘arr’ containing ‘n’ integers. You are also given an integer ‘num’, and your task is to find whether ‘num’ is present in the array or not.

    # If ‘num’ is present in the array, return the 0-based index of the first occurrence of ‘num’. Else, return -1.

    # For example:

    # Input: ‘n’ = 5, ‘num’ = 4 
    # 'arr' =  [6,7,8,4,1] 

    # Output: 3

    # Explanation:
    # 4 is present at the 3rd index.

# endregion


def linearSearch(n: int, num: int, arr: [int]) -> int:
    # Write your code here.
    for i in range(len(arr)):
        if num == arr[i]:
            return i

    return -1


# Test
n = 5       
num = 4
arr = [6, 7, 8, 4, 1]
print(linearSearch(n, num, arr))  # Output: 3   