# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

class BST:
def init__(self):
Self.tree = [None] * 100
def insert (self, data):
i=0
while 4 < 100:
if self.tree(i] is None:
self.tree(i] = data
return
if data < self.tree(i):
ie2eie2
elif data > self.tree(il:
ia2zeie2
else:
return
def inorder(self, i=0):
Af 4 < 100 and self.tree[i] is not None:
self. inorder (2 * i + 1)
print (self.tree(i], end=" ")
Self-inorder(2* i+ 2)]
def preorder(self, i=0):
if i < 100 and self.tree[i] is not None:
print (self.tree[i], end=" ")
self.preorder(2 * i + 1)
self.preorder(2 * i + 2)
def postorder(self, i=0):
if i < 100 and self.tree(i] is not None:
self.postorder(2 * i + 1)
self.postorder(2 * i + 2)
print (self.tree[i], end=" ")
def count (self) :
return sum(1 for x in self.tree if x is not None)
def height (self, i=0):
Af i >= 100 or self.tree[i] is None:
return 0
verucn 1 @ marfaei? heiahe(? * i + 1).
