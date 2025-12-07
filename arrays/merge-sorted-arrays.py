
# Merges two sorted lists a and b into a new sorted list.
# Example: a = [1, 3, 5]
#          b = [2, 4, 6]
# merge_sorted(a, b) → [1,2,3,4,5,6]

# Use 2 pointers to keep track of current index of both lists.
# Compare elements at both pointers and append the smaller element to the result list.
# Move the pointer of the list from which the element was taken.
# If one list is exhausted, append the remaining elements of the other list to the result.


# region Time Complexity
    # The time complexity of this function is O(m + n), where m and n are the number of elements
    # in the two arrays. This is because we traverse both arrays once.  
# endregion

# region Space Complexity
    # The space complexity of this function is O(m + n), where m and n are the number of elements
    # in the two arrays. This is because we are creating a new array to store the merged result.  
# endregion

def merge_sorted(a, b):
    merged = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    return merged + a[i:] + b[j:]