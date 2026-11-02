class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
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
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Insert at specific index
    def insert_index(self, data, index):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_beginning(data)
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Invalid index")
                return
            temp = temp.next

        if temp is None:
            print("Invalid index")
            return

        new_node = Node(data)
        new_node.next = temp.next
        new_node.prev = temp

        if temp.next:
            temp.next.prev = new_node

        temp.next = new_node

    # Delete by value
    def delete_value(self, data):
        temp = self.head

        while temp and temp.data != data:
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        if temp.prev:
            temp.prev.next = temp.next
        else:
            self.head = temp.next

        if temp.next:
            temp.next.prev = temp.prev

        print("Node deleted")

    # Delete at beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

        print("First node deleted")

    # Delete at end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        if temp.prev:
            temp.prev.next = None
        else:
            self.head = None

        print("Last node deleted")

    # Count nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


# Main Program
dll = DoublyLinkedList()

while True:
    print("\n----- DOUBLY LINKED LIST -----")
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
        dll.create()

    elif choice == 2:
        data = int(input("Enter value: "))
        dll.insert_beginning(data)

    elif choice == 3:
        data = int(input("Enter value: "))
        dll.insert_end(data)

    elif choice == 4:
        data = int(input("Enter value: "))
        index = int(input("Enter index: "))
        dll.insert_index(data, index)

    elif choice == 5:
        data = int(input("Enter value to delete: "))
        dll.delete_value(data)

    elif choice == 6:
        dll.delete_beginning()

    elif choice == 7:
        dll.delete_end()

    elif choice == 8:
        dll.count_nodes()

    elif choice == 9:
        dll.display()

    elif choice == 10:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
