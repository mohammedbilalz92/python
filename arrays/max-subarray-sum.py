"""Kadane's Algorithm to find the maximum subarray sum in an array.
The algorithm works by iterating through the array while keeping track of the current subarray sum
and the maximum subarray sum found so far. If the current subarray sum becomes negative,

it is reset to zero, as starting a new subarray from the next element may yield a higher sum.

it basically finds the maximum sum of contiguous subarray within a one-dimensional array of numbers.
"""

# region Time Complexity
    # The time complexity of this function is O(n), where n is the number of elements
    # in the array. This is because we traverse the array only once to find the maximum subarray sum.
# endregion

# region Space Complexity
    # The space complexity of this function is O(1) since we are using only a constant amount of extra space.
# endregion

def max_subarray(arr):
    max_ending = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending = max(x, max_ending + x)
        max_so_far = max(max_so_far, max_ending)
    return max_so_far