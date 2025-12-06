# region Time Complexity
    # The time complexity of this function is O(n), where n is the number of elements in the array.
    # This is because we traverse the array only once to find the second largest element.
# endregion

def second_largest(arr):
    """Function to find the second largest element in an array.""" 
    first = second = float('-inf')
    for x in arr:
        if x > first:
            second = first
            first = x
        elif first > x > second:
            second = x
    return second if second != float('-inf') else None


# Test
arr = [1, 2, 3, 4, 5]
print(second_largest(arr))  # Output: 4