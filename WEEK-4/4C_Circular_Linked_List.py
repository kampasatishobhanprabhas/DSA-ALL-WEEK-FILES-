class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Create linked list
    def create(self):
        n = int(input("Enter number of nodes: "))
        for i in range(n):
            data = int(input("Enter value: "))
            self.insert_end(data)

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # Insert at specific index
    def insert_index(self, data, index):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_beginning(data)
            return

        if self.head is None:
            print("Invalid index")
            return

        temp = self.head
        for i in range(index - 1):
            temp = temp.next
            if temp == self.head:
                print("Invalid index")
                return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    # Delete by value
    def delete_value(self, data):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        previous = None

        while True:
            if current.data == data:
                if current == self.head:
                    if self.head.next == self.head:
                        self.head = None
                    else:
                        last = self.head
                        while last.next != self.head:
                            last = last.next

                        self.head = self.head.next
                        last.next = self.head
                else:
                    previous.next = current.next

                print("Node deleted")
                return

            previous = current
            current = current.next

            if current == self.head:
                break

        print("Value not found")

    # Delete at beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
        else:
            last = self.head
            while last.next != self.head:
                last = last.next

            self.head = self.head.next
            last.next = self.head

        print("First node deleted")

    # Delete at end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            print("Last node deleted")
            return

        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head
        print("Last node deleted")

    # Count nodes
    def count_nodes(self):
        if self.head is None:
            print("Number of nodes: 0")
            return

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next
            if temp == self.head:
                break

        print("Number of nodes:", count)

    # Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")


# Main Program
cll = CircularLinkedList()

while True:
    print("\n----- CIRCULAR LINKED LIST -----")
    print("1. Create linked list")
    print("2. Insert at beginning")
    print("3. Insert at end")
    print("4. Insert at specific index")
    print("5. Delete by value")
    print("6. Delete at beginning")
    print("7. Delete at end")
    print("8. Count nodes")
    print("9. Display / Traverse")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cll.create()

    elif choice == 2:
        data = int(input("Enter value: "))
        cll.insert_beginning(data)

    elif choice == 3:
        data = int(input("Enter value: "))
        cll.insert_end(data)

    elif choice == 4:
        data = int(input("Enter value: "))
        index = int(input("Enter index: "))
        cll.insert_index(data, index)

    elif choice == 5:
        data = int(input("Enter value to delete: "))
        cll.delete_value(data)

    elif choice == 6:
        cll.delete_beginning()

    elif choice == 7:
        cll.delete_end()

    elif choice == 8:
        cll.count_nodes()

    elif choice == 9:
        cll.display()

    elif choice == 10:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
