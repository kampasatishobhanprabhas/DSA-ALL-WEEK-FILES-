class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full")
        else:
            if self.front == -1:
                self.front = 0

            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
            print("Inserted:", data)

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            print("Deleted:", self.queue[self.front])

            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        else:
            i = self.front

            while True:
                print(self.queue[i], end=" ")
                if i == self.rear:
                    break
                i = (i + 1) % self.size

            print()


size = int(input("Enter queue size: "))
q = CircularQueue(size)

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
