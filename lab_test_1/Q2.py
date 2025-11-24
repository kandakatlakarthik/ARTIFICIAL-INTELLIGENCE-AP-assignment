class Node:
    """Single node for the linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Singly linked list with insert at tail and delete by value."""

    def __init__(self):
        self.head = None

    def insert(self, value):
        """Insert a new node containing value at the end of the list."""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, value):
        """Delete the first occurrence of value. Returns True if removed."""
        current = self.head
        previous = None

        while current:
            if current.data == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

    def __str__(self):
        if not self.head:
            return "∅"

        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " → ".join(values)


def parse_numbers(raw_text):
    """Convert comma-separated input into a list of integers."""
    parts = [part.strip() for part in raw_text.split(",") if part.strip()]
    if not parts:
        raise ValueError("Please enter at least one number.")
    return [int(part) for part in parts]


def main():
    linked_list = LinkedList()
    print("Basic Linked List (insert/delete)")
    print("Enter comma-separated integers when prompted.\n")

    while True:
        try:
            initial_values = parse_numbers(
                input("Insert the numbers: ").strip()
            )
            break
        except ValueError as exc:
            print(f"[!] {exc}")

    for value in initial_values:
        linked_list.insert(value)
    print(f"Linked list becomes:\n{linked_list}\n")

    while True:
        action = input("Choose an action (insert/delete/exit): ").strip().lower()

        if action == "insert":
            try:
                values = parse_numbers(input("Insert the numbers: ").strip())
            except ValueError as exc:
                print(f"[!] {exc}")
                continue
            for value in values:
                linked_list.insert(value)
            print(f"Linked list becomes:\n{linked_list}\n")

        elif action == "delete":
            raw = input("Delete the number(s): ").strip()
            if not raw:
                print("[!] Please enter a number to delete.")
                continue
            try:
                values = parse_numbers(raw)
            except ValueError as exc:
                print(f"[!] {exc}")
                continue

            for value in values:
                if linked_list.delete(value):
                    print(f"Deleted {value}.")
                else:
                    print(f"{value} was not found.")
            print(f"Linked list becomes:\n{linked_list}\n")

        elif action == "exit":
            print("Exiting program.")
            break
        else:
            print("Unknown action. Please choose insert, delete, or exit.")


if __name__ == "__main__":
    main()