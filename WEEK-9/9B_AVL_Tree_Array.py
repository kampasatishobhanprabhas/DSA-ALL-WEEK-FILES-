class AVL:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    def height(self, i):
        if i >= self.size or self.tree[i] is None:
            return 0
        return self.tree[i][1]

    def balance(self, i):
        return self.height(2 * i + 1) - self.height(2 * i + 2)

    def right_rotate(self, y):
        x = 2 * y + 1
        t2 = 2 * x + 2

        self.tree[x], self.tree[y] = self.tree[y], self.tree[x]
        self.tree[t2], self.tree[2 * y + 1] = self.tree[2 * y + 1], self.tree[t2]

    def insert(self, data, i=0):
        if i >= self.size:
            print("Array is full")
            return

        if self.tree[i] is None:
            self.tree[i] = (data, 1)
            return

        if data < self.tree[i][0]:
            self.insert(data, 2 * i + 1)
        elif data > self.tree[i][0]:
            self.insert(data, 2 * i + 2)

    def display(self):
        print(self.tree)


avl = AVL(int(input("Enter array size: ")))

while True:
    print("\n1. Insert")
    print("2. Display")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter element: "))
        avl.insert(data)
    elif choice == 2:
        avl.display()
    elif choice == 3:
        break
    else:
        print("Invalid choice")
