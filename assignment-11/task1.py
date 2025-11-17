# stack_program.py

class Stack:
    """A simple Stack implementation using a Python list."""

    def __init__(self):
        """Initializes an empty stack."""
        self._items = []

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return not self._items

    def push(self, item):
        """
        Adds an item to the top of the stack.

        Args:
            item: The item to be added to the stack.
        """
        self._items.append(item)
        print(f"Pushed '{item}' to the stack.")

    def pop(self):
        """
        Removes and returns the top item of the stack.

        Returns:
            The top item of the stack, or None if the stack is empty.
        """
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        item = self._items.pop()
        print(f"Popped '{item}' from the stack.")
        return item

    def peek(self):
        """
        Returns the top item of the stack without removing it.

        Returns:
            The top item of the stack, or None if the stack is empty.
        """
        if self.is_empty():
            print("Stack is empty. Cannot peek.")
            return None
        item = self._items[-1]
        print(f"Top item is '{item}'.")
        return item

    def __str__(self):
        """Returns a string representation of the stack."""
        return f"Current Stack: {self._items}"


def main():
    """Main function to run the user-interactive stack program."""
    stack = Stack()

    while True:
        print("\n--- Stack Operations ---")
        print("1. Push an item")
        print("2. Pop an item")
        print("3. Peek at the top item")
        print("4. Check if the stack is empty")
        print("5. Display stack")
        print("6. Exit")
        print("------------------------")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            item = input("Enter the item to push: ")
            stack.push(item)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            if stack.is_empty():
                print("The stack is empty.")
            else:
                print("The stack is not empty.")
        elif choice == '5':
            print(stack)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
