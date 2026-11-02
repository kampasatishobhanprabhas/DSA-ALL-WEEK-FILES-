# Extracted from the program screenshot in the DSA manual.
# Please check indentation/symbols before running.

[BS
if root:
self.postorder (root. left)
self.postorder (root .right)
print (root.data, end="_")
def level_order (self):
if self.root is None:
return
queue = [self.root]
while queue:
node = queue.pop (0)
print (node.data, end="_")
if node.left:
queue. append (node. left)
if node.right:
queue. append (node. right)
|bt = BinaryTree()
|bt.root = Node ("A")
|bt.root.left = Node("B")
|bt.root.right = Node("C")
|bt.root.left.left = Node("D")
|bt.root.left.right = Node("E")
lprint ("preorder")
