# Stacks
stack = []

stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

print('Elements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('Stack after elements are popped:')
print(stack)

from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack:')
print(stack)

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)

from queue import LifoQueue

stack = LifoQueue(maxsize=5)

print(stack.qsize())

stack.put('a')
stack.put('b')
stack.put('c')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())

# whith linked list:
# Last in, first out:

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self) -> None:
        self.top = None

    def is_empty(self):
        return self.top is None
    
    # append data
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        return

    # Remove the top 
    def pop(self):
        if self.top is None:
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped
    
    # See the top
    def peek(self):
        if self.top is None:
            return None
        return self.top.data
    
    def length(self):
        if self.top is None:
            return 0
        cur_node = self.top
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        return count
    
    def display(self):
        if self.top is None:
            print('Your Stack is empty')
            return
        cur_node = self.top
        while cur_node is not None:
            print(cur_node.data, end=' -> ')
            cur_node = cur_node.next
        print('None')
        return
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

stack.display() 

n = stack.length()
print('the length is: ', n)

print("Peek:", stack.peek())  

print("Popped:", stack.pop())  

stack.display() 

n = stack.length()
print('the length is: ', n)




