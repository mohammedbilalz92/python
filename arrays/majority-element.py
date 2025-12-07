# Boyer Moore Voting Algorithm to find the majority element in an array.
# A majority element is an element that appears more than n/2 times in an array of size n.
# Example: arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
# majority_element(arr) → 4 (since 4 appears 5 times which is more than 9/2 = 4.5)

# region Time Complexity
    # The time complexity of this function is O(n), where n is the number of elements   
    # in the array. This is because we traverse the array only once to find the majority element. 
# endregion

# region Space Complexity
    # The space complexity of this function is O(1) since we are using only a constant amount of extra space.
# endregion

def majority_element(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate


# Test
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print(majority_element(arr))  # Output: 4

arr = [2, 2, 1, 1, 1, 2, 2]
print(majority_element(arr))  # Output: 2

