# Sorts a list of items in descending order based on their quantity
def bubble_sort(items):
    n = len(items)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if items[j].quantity < items[j + 1].quantity:
                items[j], items[j + 1] = items[j + 1], items[j]
