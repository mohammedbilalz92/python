# region Time Complexity
    # The time complexity of this function is O(n), where n is the number of elements   
    # in the array. This is because we traverse the array only once to count occurrences. 
# endregion

# region Space Complexity
    # The space complexity of this function is O(1) since we are using only a constant amount of extra space.   
# endregion

def count_occurrences(arr, target):
    count = 0
    for x in arr:
        if x == target:
            count += 1
    return count

# Test
arr = [1, 2, 3, 2, 4, 2, 5]
target = 2
print(count_occurrences(arr, target))  # Output: 3