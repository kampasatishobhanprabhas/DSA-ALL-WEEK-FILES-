class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
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
        new_node.next = self.head
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
        temp.next = new_node

    # Delete by value
    def delete_value(self, data):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            print("Node deleted")
            return

        temp = self.head
        while temp.next and temp.next.data != data:
            temp = temp.next

        if temp.next is None:
            print("Value not found")
        else:
            temp.next = temp.next.next
            print("Node deleted")

    # Delete at beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next
            print("First node deleted")

    # Delete at end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            print("Last node deleted")
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None
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
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program
ll = SinglyLinkedList()

while True:
    print("\n----- SINGLY LINKED LIST -----")
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
        ll.create()

    elif choice == 2:
        data = int(input("Enter value: "))
        ll.insert_beginning(data)

    elif choice == 3:
        data = int(input("Enter value: "))
        ll.insert_end(data)

    elif choice == 4:
        data = int(input("Enter value: "))
        index = int(input("Enter index: "))
        ll.insert_index(data, index)

    elif choice == 5:
        data = int(input("Enter value to delete: "))
        ll.delete_value(data)

    elif choice == 6:
        ll.delete_beginning()

    elif choice == 7:
        ll.delete_end()

    elif choice == 8:
        ll.count_nodes()

    elif choice == 9:
        ll.display()

    elif choice == 10:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
