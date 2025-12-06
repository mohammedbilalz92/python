# region Time Complexity
    # The time complexity of this function is O(n), where n is the number of elements in the array.
    # This is because we traverse half of the array to reverse it.
# endregion 

# region Space Complexity
    # The space complexity of this function is O(1) as we are reversing the array in place and not using any extra space.
# endregion

def reverse_array(arr):
    """Function to reverse an array."""
    start = 0
    end = len(arr) - 1

    while start < end:
        # Swap the elements at start and end indices
        arr[start], arr[end] = arr[end], arr[start]
        # Move towards the middle
        start += 1
        end -= 1

    return arr

# Test
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))  # Output: [5, 4, 3, 2, 1]
