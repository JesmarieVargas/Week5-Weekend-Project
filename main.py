from book_add import add_book
from borrow_book import borrow_book
from return_book import return_book
from book_search import book_search
from display_books import display_books
from add_user import add_user
from view_user import view_user
from display_users import display_users

def main():
    while True:
        input1 = input(''' 
                       
 Welcome to the Library Management System!
                       
1. Book Operations
2. User Operations
3. Quit
                       
 ''')
        if input1 == '1':
            book_menu()
        elif input1 == '2':
            user_menu()
        elif input == '3':
            print(" Thank you for using the Library Management System!")
            break
        else:
            print("Invalid input.")

def book_menu():
    while True:
        input1 = input('''
                       
Book Operations:
                       
        1. Add a new book
        2. Borrow a book
        3. Return a book
        4. Search for a book
        5. Display all books            
        6. Quit
                       
''')
        
        if input1 == "1":
            add_book()
        elif input1 == "2":
            borrow_book()
        elif input1 == "3":
            return_book()
        elif input1 == "4":
            book_search()
        elif input1 == "5":
            print("All books:")
            display_books()
        elif input1 == "6":
            return main()
        else:
            print("Invalid input")
            break

def user_menu():
    while True:
        input1 = input('''
           
User Operations:
                       
        1. Add a new user
        2. View user details
        3. Display all users
        4. Quit
                       
''')
        if input1 == "1":
            add_user()
        elif input1 == "2":
            view_user()
        elif input1 == "3":
           print("All Users:")
           display_users()
        elif input1 == "4":
            return main()
        else:
            print("Invalid input")
            break

main()