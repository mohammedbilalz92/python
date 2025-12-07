# rotate the array by k positions to the right

#Example:Rotate [1,2,3,4,5,6,7] by k=3 → [5,6,7,1,2,3,4]

# Approach:
# 1. Reverse the entire array.
# 2. Reverse the first k elements.
# 3. Reverse the remaining n-k elements.


# region Time Complexity
    # The time complexity of this function is O(n), where n is the number of elements
    # in the array. This is because we traverse the array a constant number of times (three reversals).
# endregion

# region Space Complexity
    # The space complexity of this function is O(1) since we are using only a constant amount of extra space.   
# endregion

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# region Time Complexity
    # The time complexity of this function is O(n), where n is the number of elements
    # in the array. This is because we traverse the array a constant number of times (three reversals). 
# endregion

# region Space Complexity
    # The space complexity of this function is O(1) since we are using only a constant amount of extra space.   
# endregion
def rotate(arr,k):
    n = len(arr)
    k = k % n  # in case k is greater than n
    reverse(arr, 0, n-1) # Step 1: Reverse the entire array
    reverse(arr, 0, k-1) # Step 2: Reverse the first k elements
    reverse(arr, k, n-1) # Step 3: Reverse the remaining n-k elements
    return arr


