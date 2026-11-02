class BinaryTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    def insert(self, data):
        for i in range(self.size):
            if self.tree[i] is None:
                self.tree[i] = data
                return
        print("Tree is full")

    def display(self):
        print("Binary Tree:", self.tree)


bt = BinaryTree(int(input("Enter size: ")))

while True:
    print("\n1. Insert")
    print("2. Display")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter element: "))
        bt.insert(data)
    elif choice == 2:
        bt.display()
    elif choice == 3:
        break
    else:
        print("Invalid choice")
