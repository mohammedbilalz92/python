# region Time Complexity
    # The time complexity of this function is O(n), where n is the number of elements in the array.
    # This is because we traverse the array only once to remove duplicates. 
# endregion

# region Space Complexity
    # The space complexity of this function is O(1) since we are using only a constant amount of extra space.   
# endregion

def remove_duplicates(nums):
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
    return j + 1

# Test

nums = [1, 1, 2, 2, 3, 4, 4]
length = remove_duplicates(nums)    
print(length)  # Output: 4

print(nums)