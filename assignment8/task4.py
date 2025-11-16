# /path/to/your/project/test_shopping_cart.py

import unittest
from shopping_cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    """
    Test cases for the ShoppingCart class.
    """

    def setUp(self):
        """
        Set up a new ShoppingCart instance before each test.
        This method is called automatically by the test runner before every single test.
        """
        self.cart = ShoppingCart()

    def test_add_single_item(self):
        """Test adding a single item to the cart."""
        self.cart.add_item("Apple", 0.50)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["name"], "Apple")
        self.assertEqual(self.cart.items[0]["price"], 0.50)

    def test_add_multiple_items(self):
        """Test adding multiple different items."""
        self.cart.add_item("Apple", 0.50)
        self.cart.add_item("Banana", 0.75)
        self.assertEqual(len(self.cart.items), 2)

    def test_add_duplicate_items(self):
        """Test adding the same item multiple times."""
        self.cart.add_item("Apple", 0.50)
        self.cart.add_item("Apple", 0.50)
        self.assertEqual(len(self.cart.items), 2)
        # Verify both instances are present
        self.assertEqual(self.cart.total_cost(), 1.00)

    def test_add_item_with_invalid_price(self):
        """Test that adding an item with a zero or negative price raises a ValueError."""
        with self.assertRaises(ValueError):
            self.cart.add_item("Bad Apple", -1.00)
        with self.assertRaises(ValueError):
            self.cart.add_item("Zero Apple", 0)

    def test_remove_item(self):
        """Test removing an item from the cart."""
        self.cart.add_item("Apple", 0.50)
        self.cart.add_item("Banana", 0.75)
        self.cart.remove_item("Apple")
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0]["name"], "Banana")

    def test_remove_item_not_in_cart(self):
        """Test that removing an item not in the cart raises a ValueError."""
        self.cart.add_item("Apple", 0.50)
        with self.assertRaises(ValueError):
            self.cart.remove_item("Banana")

    def test_remove_item_from_empty_cart(self):
        """Test that removing an item from an empty cart raises a ValueError."""
        with self.assertRaises(ValueError):
            self.cart.remove_item("Apple")

    def test_total_cost_empty_cart(self):
        """Test the total cost of an empty cart is 0."""
        self.assertEqual(self.cart.total_cost(), 0)

    def test_total_cost_with_items(self):
        """Test the total cost calculation with multiple items."""
        self.cart.add_item("Apple", 0.50)
        self.cart.add_item("Banana", 0.75)
        self.cart.add_item("Orange", 1.25)
        # Using assertAlmostEqual for floating point comparisons
        self.assertAlmostEqual(self.cart.total_cost(), 2.50)

    def test_total_cost_after_removing_item(self):
        """Test the total cost is updated after an item is removed."""
        self.cart.add_item("Apple", 0.50)
        self.cart.add_item("Banana", 0.75)
        self.cart.remove_item("Apple")
        self.assertAlmostEqual(self.cart.total_cost(), 0.75)


if __name__ == '__main__':
    unittest.main()

