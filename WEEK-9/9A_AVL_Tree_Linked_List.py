class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def height(self, root):
        if root is None:
            return 0
        return root.height

    def balance(self, root):
        if root is None:
            return 0
        return self.height(root.left) - self.height(root.right)

    def right_rotate(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def left_rotate(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)
        else:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        b = self.balance(root)

        if b > 1 and data < root.left.data:
            return self.right_rotate(root)

        if b < -1 and data > root.right.data:
            return self.left_rotate(root)

        if b > 1 and data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if b < -1 and data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)


avl = AVL()
root = None

while True:
    print("\n1. Insert")
    print("2. Inorder Traversal")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter element: "))
        root = avl.insert(root, data)
    elif choice == 2:
        avl.inorder(root)
        print()
    elif choice == 3:
        break
    else:
        print("Invalid choice")
