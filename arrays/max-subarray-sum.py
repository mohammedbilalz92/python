"""Kadane's Algorithm to find the maximum subarray sum in an array.
The algorithm works by iterating through the array while keeping track of the current subarray sum
and the maximum subarray sum found so far. If the current subarray sum becomes negative,

it is reset to zero, as starting a new subarray from the next element may yield a higher sum.

it basically finds the maximum sum of contiguous subarray within a one-dimensional array of numbers.

Kadane's sub array starts with negative only when all elements are negative.
because it hurts the sum.

e.g.
Input: [-2,1,-3,4,-1,2,1,-5,4]
Output: 6   
Maximum subarray is [4,-1,2,1] with sum 6.
Starting from 4, we keep adding elements until the sum is maximized.

e.g.
Input: [5,4,-1,7,8]
Output: 23
Maximum subarray is [5,4,-1,7,8] with sum 23.
Starting from 5, we keep adding elements until the sum is maximized.
"""

# region Time Complexity
    # The time complexity of this function is O(n), where n is the number of elements
    # in the array. This is because we traverse the array only once to find the maximum subarray sum.
# endregion

# region Space Complexity
    # The space complexity of this function is O(1) since we are using only a constant amount of extra space.
# endregion

def max_subarray_sum(arr):
    """max_ending: energy you currently have
    max_so_far: maximum energy you have ever seen

    As I move forward, my engergy should increase, if it gets negative I reset at x and if energy is positive continue.
    """
    max_ending = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending = max(x, max_ending + x) # This line decides whether to keep going or throw away the past.
        max_so_far = max(max_so_far, max_ending) # update the best so far, this keeps track of the best energy we had so far even if current energy decreases later.
    return max_so_far

# Test
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum(arr))  # Output: 6

arr = [5,4,-1,7,8]
print(max_subarray_sum(arr))  # Output: 23