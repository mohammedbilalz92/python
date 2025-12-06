# region Time Complexity
    # The time complexity of this function is O(n), where n is the number of elements
    # in the array. This is because we traverse the array only once to find the pair. 
# endregion

# region Space Complexity
    # The space complexity of this function is O(n) since we are using a set to store seen elements.   
# endregion


def find_pair(arr, target):
    seen = set()
    for num in arr:
        if (target - num ) in seen:
            return (num, target - num)
        seen.add(num)
    return None

def find_pair_return_index(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in seen:
            return (seen[diff], i)
        seen[num] = i
    return None

# Test
arr = [10, 15, 3, 7]
target = 17
print(find_pair(arr, target))  # Output: (7, 10)