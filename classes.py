from functions import bubble_sort


# Represents a node in a linked list
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


# Represents a linked list of items
class LinkedList:
    def __init__(self):
        self.head = None

    # Function to add an item to the list
    def add_item(self, item):
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Function that displays the item in the list in the format of (Item Name: Item Quantity)
    def display_items(self):
        current = self.head
        while current:
            print(f"{current.item.name}: {current.item.quantity}")
            current = current.next


# Item Class - Represents an item with a name, quantity, and total quantity
class Item:
    def __init__(self, name, quantity, total_quantity):
        self.name = name
        self.quantity = quantity
        self.total_quantity = total_quantity

    # function that displays the item in the format of (Quantity / Total Quantity Needed - Name of Item)
    def __str__(self):
        return f"{self.quantity} / {self.total_quantity} - {self.name}"


# Base Builder Class - Helps manage the items using a linked list
class BaseBuilderHelper:
    def __init__(self):
        # Linked List is used to store items
        self.items = LinkedList()

    # Function that adds and item to the linked list
    def add_item(self, item_name, item_quantity, total_quantity):
        try:
            item_quantity = int(item_quantity)
            total_quantity = int(total_quantity)
            if item_quantity <= 0 or total_quantity <= 0:
                raise ValueError("Quantities must be positive integers.")
        except ValueError:
            print("Invalid input for quantities. Please enter positive integers.")
            return

        item = Item(item_name, item_quantity, total_quantity)
        self.items.add_item(item)

    # Function that sorts the linked list
    def sort_items(self):

        # Convert linked list to a list for sorting
        items_list = []
        current = self.items.head
        while current:
            items_list.append(current.item)
            current = current.next

        # Bubble Sorting Items
        bubble_sort(items_list)

        # Update the linked list
        self.items = LinkedList()
        for item in items_list:
            self.items.add_item(item)

    # Function that displays the items
    def display_items(self):

        # Display Items
        self.sort_items()
        current = self.items.head
        while current:
            print(current.item)
            current = current.next

    # Function that increments the quantity of the item
    def increment_quantity(self, item_name, amount):
        current = self.items.head
        while current:
            if current.item.name == item_name:
                try:
                    if amount < 0:
                        raise ValueError("Increment amount cannot be negative.")
                    total_quantity = int(current.item.total_quantity)
                    current_quantity = int(current.item.quantity)
                    if current_quantity + amount <= total_quantity:
                        current.item.quantity += amount
                        return True
                    else:
                        raise ValueError("Cannot have more than the total quantity.")
                except ValueError as e:
                    print(str(e))
                    return False
            current = current.next
        print(f"Item '{item_name}' not found.")
        return False

    # Function that decrements the quantity of the item
    def decrement_quantity(self, item_name, amount):
        current = self.items.head
        while current:
            if current.item.name == item_name:
                try:
                    if amount < 0:
                        raise ValueError("Decrement amount cannot be negative.")
                    if current.item.quantity - amount < 0:
                        raise ValueError("Quantity cannot be negative.")
                    current.item.quantity -= amount
                    return True
                except ValueError as e:
                    print(str(e))
                    return False
            current = current.next
        print(f"Item '{item_name}' not found.")
        return False

    # Function that removes the item in its entirety
    def remove_item(self, item_name):
        current = self.items.head
        prev = None
        while current:
            if current.item.name == item_name:
                if prev:
                    prev.next = current.next
                else:
                    self.items.head = current.next
                return True
            prev = current
            current = current.next
        return False
