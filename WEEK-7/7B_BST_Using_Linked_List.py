class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")


bst = BST()

while True:
    print("\n1. Insert")
    print("2. Inorder")
    print("3. Preorder")
    print("4. Postorder")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter element: "))
        bst.root = bst.insert(bst.root, data)
    elif choice == 2:
        bst.inorder(bst.root)
        print()
    elif choice == 3:
        bst.preorder(bst.root)
        print()
    elif choice == 4:
        bst.postorder(bst.root)
        print()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
