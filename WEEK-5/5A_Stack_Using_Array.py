# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

class Stack:
def init__(self, size):
self.stack = [)
self.size = size
# Push operation
def push(self, value):
if len(self.stack) == self.size:
print ("Stack Overflow")
else:
self.stack.append (value)
print(value, "pushed into stack")
# Pop operation
def pop(self) :
if len(self.stack) == 0:
print ("Stack Underflow")
else:
value = self.stack.pop()
print ("Popped element:", value)
# Peek operation
def peek(self) :
if len(self.stack) == 0:
print ("Stack is empty")
else:
print ("Top element:", self.stack[-1])
