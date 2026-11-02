# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

queue elements.
class CircularQueue:
def init__(self, size):
Belf.size = size
self.queue = [None] * size
self.front = -1
self.rear = -1
def enqueue (self, item):
if (self.rear + 1) % self.size == self.front:
print ("Queue Overflow")
elif self.front == -1:
self.front = 0
self.rear = 0
self.queue[self.rear] = item
print (item, "inserted into the queue")
else:
self.rear = (self.rear + 1) % self.size
self.queue(self.rear] = item
print (item, "inserted into the queue")
def dequeue (self):
if self.front == -1:
print ("Queue Underflow")
elif self.front == self.rear:
item = self.queue (self. front]
self.queue(self.front] = None
self.front = -1
self.rear = -1
print (item, “deleted from the queue")
else:
jtem = self.anenelself. front]
