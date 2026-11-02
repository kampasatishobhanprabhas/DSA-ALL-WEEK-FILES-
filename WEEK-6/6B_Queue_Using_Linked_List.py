# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

ba MM
[class Queue:
def _init__(self, size=5):
Belt.size = size
self.queue = [None] * size
self.front = -1
self.rear = -1
def enqueue (self, x):
if self.rear == self.size - 1:
print ("Queue Overflow")
else:
if self.front == -1:
self.front = 0
self.rear #= 1
self.queue(self.rear] = x
print (£"(x) inserted into the queue")
def dequeue (self):
if self.front == -1 or self.front > self.rear:
print ("Queue Underflow")
else:
x = self.queue[self. front]
self.queue[self. front] = None
self.front += 1
print(f"{x} deleted from the queue")
if self.front > self.rear:
self.front = -1
self.rear = -1
def peek(self) :
if self.front == -1:
print ("Queue is empty")
else:
print ("Front element:", self.queue(self.front])
def display(self):
if self.front == -1:
print ("Queue is empty")
else:
