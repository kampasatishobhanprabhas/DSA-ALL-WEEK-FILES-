class BST:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    def insert(self, data):
        if self.tree[0] is None:
            self.tree[0] = data
            return

        i = 0

        while i < self.size:
            if data < self.tree[i]:
                left = 2 * i + 1
                if left >= self.size:
                    print("Array is full")
                    return
                if self.tree[left] is None:
                    self.tree[left] = data
                    return
                i = left

            elif data > self.tree[i]:
                right = 2 * i + 2
                if right >= self.size:
                    print("Array is full")
                    return
                if self.tree[right] is None:
                    self.tree[right] = data
                    return
                i = right

            else:
                print("Duplicate element")
                return

    def inorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.inorder(2 * i + 1)
            print(self.tree[i], end=" ")
            self.inorder(2 * i + 2)

    def preorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            print(self.tree[i], end=" ")
            self.preorder(2 * i + 1)
            self.preorder(2 * i + 2)

    def postorder(self, i=0):
        if i < self.size and self.tree[i] is not None:
            self.postorder(2 * i + 1)
            self.postorder(2 * i + 2)
            print(self.tree[i], end=" ")


size = int(input("Enter array size: "))
bst = BST(size)

while True:
    print("\n1. Insert")
    print("2. Inorder")
    print("3. Preorder")
    print("4. Postorder")
    print("5. Display array")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter element: "))
        bst.insert(data)
    elif choice == 2:
        bst.inorder()
        print()
    elif choice == 3:
        bst.preorder()
        print()
    elif choice == 4:
        bst.postorder()
        print()
    elif choice == 5:
        print(bst.tree)
    elif choice == 6:
        break
    else:
        print("Invalid choice")
