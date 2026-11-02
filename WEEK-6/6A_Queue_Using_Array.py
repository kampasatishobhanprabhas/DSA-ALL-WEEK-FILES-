class Queue:
    def __init__(self):
        self.queue = []
        self.front = 0
        self.rear = -1

    def enqueue(self, data):
        self.queue.append(data)
        self.rear += 1
        print("Inserted:", data)

    def dequeue(self):
        if self.front > self.rear:
            print("Queue is empty")
        else:
            print("Deleted:", self.queue[self.front])
            self.front += 1

    def display(self):
        if self.front > self.rear:
            print("Queue is empty")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


q = Queue()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter element: "))
        q.enqueue(data)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
