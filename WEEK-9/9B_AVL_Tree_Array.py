# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

Ba A i EE. A, Mn.
class AVLTree:
def init__(self, size=100):
Seif.size = size
self.tree = [None] * size
self-height = (0] * size
def get_height (self, i):
fT <0 or i >= self.size or self.tree{i] is sone:
return 0
return self-height [i]
def update_height (self, i):
self.height(i] = 1 + max(
self.get_height (2 * i+ 1),
self.get_height (2 * 4 + 2)
)
def get_palance(self, i):
if T >= self.size or self.tree{i} is wone:
return 0
return self.get_neight (2 * 4+ 1) - self.get_neignt(2 * 4 + 2)
# Right Rotation
def right_rotate(self, i):
left =2*i +1
right =2*i+2
if left >= self.size or self.tree[left] is None:
return i
new_root = left
‘temp = 2 * new_root + 2
self.tree(temp] = self.tree(right) if right < self.size else sone
self-height(temp] = self.height{right] if right < self.size else 0
self.tree{right] = self.tree(i]
self-height [right] = self-height (il
self.tree[i] = self.tree{new_root]
self height [i] = self.height{new root)
self.tree{new_root] = None
self-height [néw_root] = 0
return i
