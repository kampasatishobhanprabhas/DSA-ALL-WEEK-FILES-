# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

| A. *week_7.py - C/Users/shobh/AppData/Local/Programs/Python/Python3 14/week_7.py (3.14.7)*
class BST:
def _ init__(self):
Self.tree = [None] * 100
def insert(self, data):
i-o
while i < 100:
if self.tree[i] is None:
self.tree[i] = data
print ("Element inserted")
return
if data < self.tree[i]:
is2*iea
elif data > self.tree[i]:
ia2*ie2
else:
print ("Duplicate elements not allowed")
return
print("Tree is full")
def search(self, data):
iso
while i < 100 and self.tree[i] is not None:
if self.tree[i] == data:
return True
