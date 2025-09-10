d = {}  # Dictionary to store book ID and title

def library(d):
    for i in range(4):
        bookid = int(input("Enter book id: "))
        bname = input("Enter book name: ")
        d[bookid] = bname
    print(d)

def add(book_id, name):
    d[book_id] = name
    print("Book added.")
    print(d)

def rem(book_id):
    if book_id in d:
        d.pop(book_id)
        print("Book removed.")
    else:
        print("Book ID not found.")
    print(d)

def search(book_id):
    if book_id in d:
        print(f'Book ID {book_id} with name "{d[book_id]}" is available.')
    else:
        print(f'Book ID {book_id} is not available.')

def update(book_id):
    if book_id in d:
        new_title = input("Enter the new title for the book: ")
        d[book_id] = new_title
        print("Book title updated.")
    else:
        print(f'Book ID {book_id} is not available.')

def display():
    if d:
        print("Current Library:")
        for id, name in d.items():
            print(f'ID: {id}, Title: {name}')
    else:
        print("Library is empty.")

def count():
    print(f'Total number of books: {len(d)}')

def booktitle(name):
    if name in d.values():
        print(f'"{name}" is available in the library.')
    else:
        print(f'"{name}" is not available in the library.')

def print_menu():
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book by ID")
    print("4. Update Book Title")
    print("5. Display All Books")
    print("6. Total Number of Books")
    print("7. Check Book by Title")
    print("8. Exit")

# Main Program Loop
while True:
    print_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Enter book ID: "))
        name = input("Enter book name: ")
        add(book_id, name)
    elif choice == 2:
        book_id = int(input("Enter book ID: "))
        rem(book_id)
    elif choice == 3:
        book_id = int(input("Enter book ID: "))
        search(book_id)
    elif choice == 4:
        book_id = int(input("Enter book ID: "))
        update(book_id)
    elif choice == 5:
        display()
    elif choice == 6:
        count()
    elif choice == 7:
        name = input("Enter book name: ")
        booktitle(name)
    elif choice == 8:
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 8.")
