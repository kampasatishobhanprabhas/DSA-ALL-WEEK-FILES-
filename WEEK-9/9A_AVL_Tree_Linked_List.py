# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

|class Node:
def init__(self, data):
self.data = data
self.left = None
self.right = None
self.height = 1
|class AVLTree:
def height (self, root):
if root is None:
return 0
return root.height
def get_balance(self, root):
if root is None:
return 0
return self.height (root.left) - self.height (root.right)
def update_height(self, root):
root.height = 1 + max(
self.height (root. left),
self.height (root.right)
.
# Right Rotation
def right_rotate(self, root):
