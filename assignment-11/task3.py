# linked_list_program.py

class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        """
        Initializes a Node.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None

class SinglyLinkedList:
    """A simple Singly Linked List implementation."""

    def __init__(self):
        """Initializes an empty linked list."""
        self.head = None

    def insert_at_beginning(self, data):
        """
        Inserts a new node with the given data at the beginning of the list.

        Args:
            data: The data for the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted '{data}' at the beginning.")

    def insert_at_end(self, data):
        """
        Inserts a new node with the given data at the end of the list.

        Args:
            data: The data for the new node.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Inserted '{data}' at the end.")
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        print(f"Inserted '{data}' at the end.")

    def display(self):
        """Displays the elements of the linked list."""
        if not self.head:
            print("The linked list is empty.")
            return

        elements = []
        current_node = self.head
        while current_node:
            elements.append(str(current_node.data))
            current_node = current_node.next
        print("Linked List: " + " -> ".join(elements))


def main():
    """Main function to run the user-interactive linked list program."""
    linked_list = SinglyLinkedList()

    while True:
        print("\n--- Singly Linked List Operations ---")
        print("1. Insert at the beginning")
        print("2. Insert at the end")
        print("3. Display the list")
        print("4. Exit")
        print("-----------------------------------")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            item = input("Enter the item to insert at the beginning: ")
            linked_list.insert_at_beginning(item)
        elif choice == '2':
            item = input("Enter the item to insert at the end: ")
            linked_list.insert_at_end(item)
        elif choice == '3':
            linked_list.display()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()