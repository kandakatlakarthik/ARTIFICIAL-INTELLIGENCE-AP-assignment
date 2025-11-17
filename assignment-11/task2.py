# queue_program.py
import collections

class Queue:
    """
    A simple Queue implementation.

    This implementation uses collections.deque for efficient appends and pops
    from both ends of the underlying data structure (O(1) time complexity).
    """

    def __init__(self):
        """Initializes an empty queue."""
        self._items = collections.deque()

    def is_empty(self):
        """
        Checks if the queue is empty.

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return not self._items

    def enqueue(self, item):
        """
        Adds an item to the end (rear) of the queue.

        Args:
            item: The item to be added to the queue.
        """
        self._items.append(item)
        print(f"Enqueued '{item}' to the queue.")

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.

        Returns:
            The front item of the queue, or None if the queue is empty.
        """
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        item = self._items.popleft()
        print(f"Dequeued '{item}' from the queue.")
        return item

    def peek(self):
        """
        Returns the front item of the queue without removing it.

        Returns:
            The front item of the queue, or None if the queue is empty.
        """
        if self.is_empty():
            print("Queue is empty. Cannot peek.")
            return None
        item = self._items[0]
        print(f"Front item is '{item}'.")
        return item

    def __str__(self):
        """Returns a string representation of the queue."""
        return f"Current Queue (Front -> Rear): {list(self._items)}"


def main():
    """Main function to run the user-interactive queue program."""
    queue = Queue()

    while True:
        print("\n--- Queue Operations ---")
        print("1. Enqueue an item")
        print("2. Dequeue an item")
        print("3. Peek at the front item")
        print("4. Check if the queue is empty")
        print("5. Display queue")
        print("6. Exit")
        print("------------------------")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            item = input("Enter the item to enqueue: ")
            queue.enqueue(item)
        elif choice == '2':
            queue.dequeue()
        elif choice == '3':
            queue.peek()
        elif choice == '4':
            if queue.is_empty():
                print("The queue is empty.")
            else:
                print("The queue is not empty.")
        elif choice == '5':
            print(queue)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
