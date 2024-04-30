import unittest
from classes import BaseBuilderHelper


class TestBaseBuilderHelper(unittest.TestCase):
    def setUp(self):
        self.builder = BaseBuilderHelper()

    @staticmethod
    def count_items(linked_list):
        count = 0
        current = linked_list.head
        while current:
            count += 1
            current = current.next
        return count

    def test_add_item(self):
        self.builder.add_item("TestItem", 5, 10)
        self.assertEqual(self.count_items(self.builder.items), 1)
        self.assertEqual(self.builder.items.head.item.name, "TestItem")

    def test_increment_quantity(self):
        self.builder.add_item("TestItem", 5, 10)
        self.builder.increment_quantity("TestItem", 3)
        self.assertEqual(self.builder.items.head.item.quantity, 8)

    def test_decrement_quantity(self):
        self.builder.add_item("TestItem", 10, 20)
        self.builder.decrement_quantity("TestItem", 3)
        self.assertEqual(self.builder.items.head.item.quantity, 7)

    def test_decrement_quantity_negative(self):
        self.builder.add_item("TestItem", 5, 10)
        self.assertFalse(self.builder.decrement_quantity("TestItem", 7))
        self.assertEqual(self.builder.items.head.item.quantity, 5)

    def test_remove_item(self):
        self.builder.add_item("TestItem", 5, 10)
        self.assertTrue(self.builder.remove_item("TestItem"))
        self.assertEqual(self.count_items(self.builder.items), 0)


if __name__ == "__main__":
    unittest.main()
