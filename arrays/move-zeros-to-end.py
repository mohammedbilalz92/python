# region Time Complexity
    # The time complexity of this function is O(n), where n is the number of elements
    # in the array. This is because we traverse the array only once to move zeros to the end. 
# endregion

# region Space Complexity
    # The space complexity of this function is O(1) since we are using only a constant amount of extra space.   
# endregion


def move_zeros(arr):
    """ j marks the position where the next non-zero element should be placed.
    i is to loop through array one at a time
    zero elements are never moved forward, only non-zero elements are swapped with the element at j index
    """
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return arr

def move_zeros_alternate(arr):
    """ This method avoid redundant swaps when the first element is non-zero """
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            if i != j:
                arr[j], arr[i] = arr[i], arr[j]
            j += 1
    return arr

def move_zeros_compact(arr):
    """ This method does not swaps at all and instead fills non-zero elements at the front
    """
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            if i != j:
                arr[i] = 0
            j += 1
    return arr

# Test
arr = [0, 1, 0, 3, 12]  
print(move_zeros(arr))  # Output: [1, 3, 12, 0, 0]
