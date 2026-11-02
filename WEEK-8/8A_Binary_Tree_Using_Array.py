# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

[class BinaryTree:
def _init_ (self):
Self.tree = [None] * 7
def preorder(self, i=0):
if i <7 and self.tree[i] is not None:
print (self.tree[i], end="")
self.preorder(2 * i + 1)
self.preorder(2 * i + 2)
def inorder(self, i=0):
if i <7 and self.tree[i] is not None:
self.inorder(2 * i + 1)
print (self.tree[i], end="_")
self.inorder(2 * i + 2)
def postorder(self, i=0):
if i <7 and self.tree[{i] is not None:
self.postorder(2 * i + 1)
self.postorder(2 * i + 2)
print (self.tree[i], end=" ")
def level_order (self):
for x in self.tree:
if x is not None:
print (x, end="_")
