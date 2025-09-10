items = ["laptop", "mobile"]

def add(n):
    items.append(n)
    print(f'"{n}" added successfully.\n')

def rem(n):
    if n in items:
        items.remove(n)
        print(f'"{n}" removed successfully.\n')
    else:
        print(f'"{n}" not found in the list.\n')

def search(n):
    if n in items:
        print(f'"{n}" is available.\n')
    else:
        print(f'"{n}" is not available.\n')

def display():
    print("Current Items:", items, "\n")

def total_number():
    print("Total number of items:", len(items), "\n")

def sort_():
    items.sort()
    print("Sorted items:", items, "\n")

def clear_():
    items.clear()
    print("Cart after clearing:", items, "\n")

def print_menu():
    print("1. Add item")
    print("2. Remove item")
    print("3. Search item")
    print("4. Display items")
    print("5. Total number of items")
    print("6. Sort items")
    print("7. Clear the items")
    print("8. Exit")

while True:
    print_menu()
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_item = input("Enter item to add: ").lower()
        add(add_item)
    elif choice == 2:
        remove_item = input("Enter item to remove: ").lower()
        rem(remove_item)
    elif choice == 3:
        search_item = input("Enter item to search: ").lower()
        search(search_item)
    elif choice == 4:
        display()
    elif choice == 5:
        total_number()
    elif choice == 6:
        sort_()
    elif choice == 7:
        clear_()
    elif choice == 8:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.\n")
