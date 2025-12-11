# region Problem Statement
    # This is famouse Floyd's Tortoise and Hare (Cycle Detection) algorithm to find duplicate in array
    # It’s one of the most mind-bending DSA problems because it uses a cycle detection trick on an array.

    # Key Insight:
    # Every number in the array is between 1 and n (inclusive), where n is the length of the array minus one.
    # This means we can treat the array as a linked list where each index points to the value at that index.
    # Since there is a duplicate, there must be a cycle in this "linked list".

    # and Array has n+1 numbers

    # Visualization:
    # Consider the array: [3, 1, 3, 4, 2]
    # Index:        0  1  2  3  4
    # Value:        3  1  3  4  2
    # We can visualize the "linked list" as:
    # Convert each value into a pointer:

    # From index 0 → go to index 3
    # From index 1 → go to index 1
    # From index 2 → go to index 3
    # From index 3 → go to index 4
    # From index 4 → go to index 2
    # This creates a cycle: 3 → 4 → 2 → 3 ...

    # The cycle starts at 3
    # And the duplicate number is 3.

    # So what does the algorithm do?
    # It detects the cycle, Then returns the start of the cycle, Which is the duplicate number.

    # Intereseting ex: [3,1,4,3,2] here since 3 is at index 0 and index 3, so both point to index 3, thus forming a cycle.
    # this finishes when both pointers meet at index 3, and the duplicate number is 3.
# endregion

# region Time Complexity
    # The time complexity of this algorithm is O(n) because we traverse the array a constant number of times.
# endregion

# region Space Complexity
    # The space complexity is O(1) because we use only a fixed amount of extra space for the pointers.
# endregion

def find_duplicate(nums):
    slow = fast = nums[0]

    # Phase 1
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Phase 2
    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
