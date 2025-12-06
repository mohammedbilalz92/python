# region Time Complexity
    # The time complexity of this function is O(n), where n is the number of elements in the array.
    # This is because we traverse the array only once to check if it is sorted. 
# endregion

def is_sorted(arr):
    """Check if the given array is sorted in non-decreasing order."""
    for i in range(len(arr) -1 ):
        if arr[i] > arr[i+1]:
            return False
    return True

# Test
arr1 = [1, 2, 2, 3, 4]
print(is_sorted(arr1))  # Output: True  