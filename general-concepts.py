# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# %% Basic Algorithm and its time complexity

# find min val in the array
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
        
# %% Stack Implementation using Linked Lists
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack_LL:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def stackSize(self):
        return self.size
    
    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return 'Stack is Empty'
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value
    
    def peek(self):
        if self.isEmpty():
            return 'Stack is Empty'
        return self.head.value
    
    def traverseAndPrint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
        print()
        
# Usage
print('******* Stack Using Linked List example **********')
myStackLL = Stack_LL()
myStackLL.push('A')
myStackLL.push('B')
myStackLL.push('C')
myStackLL.traverseAndPrint()
print("Peek: ", myStackLL.peek())
print("Pop: ", myStackLL.pop())
print("LinkedList after Pop: ", end="")
myStackLL.traverseAndPrint()
print("isEmpty: ", myStackLL.isEmpty())
print("Size: ", myStackLL.stackSize())
    
# %% Queue Implementation using List
queue = []

#Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print('Queue: ', queue)

#Peek
frontElement = queue[0]
print('Peek: ', frontElement)

#Dequeue
poppedElement = queue.pop(0)
print('Dequeue: ', poppedElement)

# Queue after Dequeue
print('Queue After Dequque: ', queue)

# isEmpty
isEmpty = not bool(queue)
print('IsEmpty: ', isEmpty)

# size
print('Queue size: ', len(queue))

# %% Dedicated Queue Class
class Queue:
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def enqueue(self, value):
        self.queue.append(value)
        
    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        return self.queue.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return 'Queue is empty'
        return self.queue[0]

# usage
# create queue
myQueue = Queue()
myQueue.enqueue('a')
myQueue.enqueue('b')
myQueue.enqueue('c')
print('Queue: ', myQueue.queue)
myQueue.dequeue()
print('Queue after dequeue: ', myQueue.queue)
print('Queue Peek: ', myQueue.peek())
print('IsEmpty: ', myQueue.isEmpty())
print('Size: ', myQueue.size())