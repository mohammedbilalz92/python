# region Time Complexity
    # The time complexity of this function is O(n), where n is the number of elements in the array.
    # This is because we calculate the sum of the array elements in a single pass.
# endregion

# region Space Complexity
    # The space complexity of this function is O(1) since we are using only a constant amount of extra space.   
# endregion

def missing_number(arr,n):
    expected = n*(n+1)//2
    actual = sum(arr)
    return expected - actual


#Test
arr = [0, 1, 2, 4, 5]   
n = 5
print(missing_number(arr, n))  # Output: 3

# Test case 2
arr = [3, 0, 1] 
n = 3
print(missing_number(arr, n))  # Output: 2