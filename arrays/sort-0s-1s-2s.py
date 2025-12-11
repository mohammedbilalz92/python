# region Problem Statement Dutch National Flag Algorithm
    # This is the Dutch National Flag Algorithm, used to sort an array of 0s, 1s, and 2s in one pass, with no extra space.

    # Sort an array containing only:
    # 0 = Red  
    # 1 = White  
    # 2 = Blue

    # into: [0s] [1s] [2s]

    # we already know the array only contains 0s, 1s, and 2s.
    # we can use the middle pointer to traverse the array.
    # if we find a 0, we swap it with the low pointer and increment both low
    # if we find a 1, we just increment the mid pointer
    # if we find a 2, we swap it with the high pointer and decrement high pointer, however we do not increment mid pointer in this case because the swapped element from high pointer needs to be checked.
# endregion

# region Time Complexity
    # The time complexity of this algorithm is O(n) because we traverse the array only once
# endregion

# region Space Complexity
    # The space complexity is O(1) because we use only a fixed amount of extra space for the pointers.
# endregion

def sort_0s_1s_2s(arr):
    low , mid, high = 0,0, len(arr)-1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return arr