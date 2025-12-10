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

    



while True:
    print("1. Add item")
    print("2. Remove item")
    print("3. Search item")
    print("4. Display items")
    print("5. Total number of items")
    print("6. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_item = input("Enter item to add: ")
        add(add_item)
    elif choice == 2:
        remove_item = input("Enter item to remove: ")
        rem(remove_item)
    elif choice == 3:
        search_item = input("Enter item to search: ")
        search(search_item)
    elif choice == 4:
        display()
    elif choice == 5:
        total_number()
    elif choice == 6:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.\n")
