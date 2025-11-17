# bst_program.py

class Node:
    """A node in a Binary Search Tree."""
    def __init__(self, key):
        """
        Initializes a Node.

        Args:
            key: The key/value to be stored in the node. Must be comparable.
        """
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """A simple Binary Search Tree implementation."""

    def __init__(self):
        """Initializes an empty BST."""
        self.root = None

    def insert(self, key):
        """
        Public method to insert a new key into the BST.

        Args:
            key: The key to insert.
        """
        if self.root is None:
            self.root = Node(key)
            print(f"Inserted '{key}' as the root.")
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        """
        Private helper method to recursively find the correct spot and insert the key.
        """
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
                print(f"Inserted '{key}' to the left of '{current_node.key}'.")
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
                print(f"Inserted '{key}' to the right of '{current_node.key}'.")
            else:
                self._insert_recursive(current_node.right, key)
        else:
            # Key already exists in the tree
            print(f"Key '{key}' already exists. Ignoring.")

    def inorder_traversal(self):
        """
        Public method to perform an in-order traversal of the BST.
        Returns a list of keys in ascending order.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, current_node, result):
        """
        Private helper method to recursively perform in-order traversal.
        """
        if current_node:
            self._inorder_recursive(current_node.left, result)
            result.append(current_node.key)
            self._inorder_recursive(current_node.right, result)


def main():
    """Main function to run the user-interactive BST program."""
    bst = BinarySearchTree()

    while True:
        print("\n--- Binary Search Tree Operations ---")
        print("1. Insert a number")
        print("2. Display in-order traversal")
        print("3. Exit")
        print("-----------------------------------")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            item_str = input("Enter the number to insert: ")
            try:
                item = int(item_str)
                bst.insert(item)
            except ValueError:
                print("Invalid input. Please enter an integer.")
        elif choice == '2':
            traversal = bst.inorder_traversal()
            if not traversal:
                print("The tree is empty.")
            else:
                # The result of in-order traversal is a sorted list of the keys
                print("In-order Traversal: " + " -> ".join(map(str, traversal)))
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
