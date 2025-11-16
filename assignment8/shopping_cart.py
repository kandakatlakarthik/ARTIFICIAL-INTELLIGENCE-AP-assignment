# /path/to/your/project/shopping_cart.py

class ShoppingCart:
    """
    A simple class to represent a shopping cart.
    """
    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = []

    def add_item(self, name: str, price: float):
        """
        Adds an item to the shopping cart.

        Args:
            name (str): The name of the item.
            price (float): The price of the item.

        Raises:
            ValueError: If the price is not a positive number.
        """
        if price <= 0:
            raise ValueError("Price must be a positive number.")
        self.items.append({"name": name, "price": price})
        # print(f"Added '{name}' to the cart.") # Commented out to keep test output clean

    def remove_item(self, name: str):
        """
        Removes the first occurrence of an item from the shopping cart.

        Args:
            name (str): The name of the item to remove.

        Raises:
            ValueError: If the item is not found in the cart.
        """
        item_to_remove = None
        for item in self.items:
            if item["name"] == name:
                item_to_remove = item
                break
        
        if item_to_remove:
            self.items.remove(item_to_remove)
            # print(f"Removed '{name}' from the cart.") # Commented out to keep test output clean
        else:
            raise ValueError(f"Item '{name}' not found in the cart.")

    def total_cost(self) -> float:
        """
        Calculates the total cost of all items in the cart.

        Returns:
            float: The total cost.
        """
        return sum(item["price"] for item in self.items)