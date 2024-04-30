from classes import BaseBuilderHelper

if __name__ == "__main__":
    builder = BaseBuilderHelper()

    print("================================")
    print("\033[31mWelcome to the Builder Assistant\033[0m")
    print("================================")
    while True:

        # GUI Input allowing the user to choose what to do with their List
        choice = input("\n\033[32m'APPEND' an item to your list \n'ADD' increase your current amount out "
                       "of the items needed \n'SUBTRACT' decrease your current amount of the needed items \n'DISPLAY' "
                       "to display items \n'REMOVE' to remove an item \n'Q' to quit\033[0m \n Enter your choice: ")

        # APPEND - APPEND an item to the list, allowing the user to add another named item with quantity and
        # total needed to the list
        if choice.upper() == 'APPEND':
            gui_item = input("\nPlease enter the item name you wish to add to the list: ")
            gui_item_quantity = input("Please enter the item quantity you currently have: ")
            total_quantity = input("Please enter the total quantity you need for this item: ")

            if not gui_item_quantity.isdigit() or not total_quantity.isdigit():
                print("Invalid input. Quantities must be positive integers.")
                continue

            builder.add_item(gui_item, gui_item_quantity, total_quantity)

        # ADD - ADD an item quantity to the desired item in the list increasing the quantity of what you have
        elif choice.upper() == 'ADD':
            item_to_increment = input("\nEnter the name of the item amount you want to add: ")
            increment_amount = int(input("Enter the quantity to add: "))
            builder.increment_quantity(item_to_increment, increment_amount)

        # SUBTRACT - SUBTRACT an item quantity to the desired item in the list decreasing the quantity of what you have
        elif choice.upper() == 'SUBTRACT':
            item_to_decrement = input("\nEnter the name of the item amount you want to subtract: ")
            decrement_amount = int(input("Enter the quantity to subtract: "))
            builder.decrement_quantity(item_to_decrement, decrement_amount)

        # DISPLAY - DISPLAY simply shows every item in the list
        elif choice.upper() == 'DISPLAY':
            print("")
            builder.display_items()

        # REMOVE - REMOVES a named item from the list entirely
        elif choice.upper() == 'REMOVE':
            item_to_remove = input("\nEnter the name of the item you want to remove: ")
            if builder.remove_item(item_to_remove):
                print(f"{item_to_remove} removed successfully.")
            else:
                print(f"\nItem '{item_to_remove}' not found in the list.")

        # Q - Quits the Program
        elif choice.upper() == 'Q':
            print("\033[31mExiting...\033[0m")
            break

        # Input Validation catch statement
        else:
            print("\nInvalid choice. Please try again.")
