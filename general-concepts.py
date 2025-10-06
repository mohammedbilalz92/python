# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("Hello, World!")

# %% Basic Algorithm and its time complexity

# fin min val in the array
arr = [2,11,1,6,8]
minValue = arr[0]
for i in arr:
    if i < minValue:
        minValue = i
        
print(minValue)

# Time complexity is how much time an algorithm takes to run relative to the size of the data set.
"""
I the example above the time algorithm needs to run is proportional to the size of the data set
this is because alg must visit every element one time to find the lowest value.

The loop must run 5 times since there are 5 items in the list
"""



# %% Stack Implementation using List
stack = []

# Push
stack.append('A')
stack.append('B')
stack.append('C')
print('Stack:', stack)

# Peek
topElement = stack[-1]
print('Peek: ', topElement)
print(stack)

# Pop
poppedElement = stack.pop()
print('Pop: ', poppedElement)
print('Stack after pop: ', stack)

# isEmpty
isEmpty = not bool(stack)
print('isEmpty: ', isEmpty)

# Size
print('Size: ', len(stack))


# %% Dedicated Stack Class
class Stack:
    def __init__(self):
        self.stack = [] #note unlike, c, java, array are not fixed size so we do not mentioned size here, it allocates memory dynamically
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def push(self, element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return 'Stack is Empty'
        return self.stack[-1]

# usage
myStack = Stack()
myStack.push(1)
myStack.push('A')
myStack.push(True)

print('Stack: ', myStack.stack)
print('Pop: ', myStack.pop())
print('Peek: ', myStack.peek())
print('isEmpty: ', myStack.isEmpty())
print('Size: ', myStack.size())
        
        