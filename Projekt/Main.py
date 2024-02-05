
import sys
from BooksDatabase import BooksDatabase
import os

db = BooksDatabase("books_database.json")
def getAllRecords():
    DisplayData(db.list_books())
def DisplayData(books):

    if len(books)!=0:
        book_id_width = max(len("Book ID"), max(len(str(book.book_id)) for book in books)) + 2
        title_width = max(len("Title"), max(len(book.title) for book in books)) + 2
        author_fn_width = max(len("Author First Name"), max(len(book.author_first_name) for book in books)) + 2
        author_ln_width = max(len("Author Last Name"), max(len(book.author_last_name) for book in books)) + 2
        pub_year_width = max(len("Publication Year"), max(len(str(book.publication_year)) for book in books)) + 2


        header = f"| {'Book ID':<{book_id_width}} | {'Title':<{title_width}} | {'Author First Name':<{author_fn_width}} | {'Author Last Name':<{author_ln_width}} | {'Publication Year':<{pub_year_width}} |"
        divider = "-" * len(header)
        print(divider)
        print(header)
        print(divider)


        for book in books:
            print(f"| {book.book_id:<{book_id_width}} | {book.title:<{title_width}} | {book.author_first_name:<{author_fn_width}} | {book.author_last_name:<{author_ln_width}} | {book.publication_year:<{pub_year_width}} |")
        print(divider)
    else:
        print("Not found")


menu_options = [
    ('1', 'Add record'),
    ('2', 'Delete record'),
    ('3', 'Search by name'),
    ('4', 'Search by second name'),
    ('5', 'Search by year'),
    ('6', 'Search by Title'),
    ('7', 'Show all records'),
    ('8', 'Exit')
]
allRecords_options = [
    ('1', 'Back to menu'),
]
def print_menu_table(menu_options):



    option_width = max(len(option[0]) for option in menu_options) + 2
    description_width = max(len(option[1]) for option in menu_options) + 2


    print(f"+{'-' * option_width}+{'-' * description_width}+")
    print(f"|{'Menu':^{option_width}}|{'Description':^{description_width}}|")
    print(f"+{'-' * option_width}+{'-' * description_width}+")


    for option, description in menu_options:
        print(f"|{option:^{option_width}}|{description:<{description_width}}|")


    print(f"+{'-' * option_width}+{'-' * description_width}+")

def get_book_data_from_user():
    print("Please enter the book details:")
    title = input("Title: ")
    author_first_name = input("Author's First Name: ")
    author_last_name = input("Author's Last Name: ")
    publication_year = input("Publication Year: ")

    db.insert_book(title,author_first_name,author_last_name,publication_year)


def delete_book_by_id():
    print("Please enter the book id:")
    id = int(input("Id: "))
    db.delete_book(id)

def find_book_by_name():
    print("Please enter the name:")
    name = input("Name: ")
    DisplayData(db.find_book_by_author_first_name(name))

def find_book_by_second_name():
    print("Please enter the second name:")
    name = input("name: ")
    DisplayData(db.find_book_by_author_last_name(name))

def find_book_by_year():
    print("Please enter the book year:")
    year = int(input("Year: "))
    DisplayData(db.find_book_by_year(year))

def find_book_by_title():
    print("Please enter the book title:")
    title = input("Title: ")
    DisplayData(db.find_book_by_title(title))



def get_number(menu_options):
    while True:
        print_menu_table(menu_options)
        data = input("Please enter a number: ")
        try:
            number = float(data)
            return number
        except ValueError:
            print("The entered data is not a number. Please try again.")




while(True):
    os.system('clear')
    choose=get_number(menu_options)

    if choose==1:
        os.system('clear')
        get_book_data_from_user()
    elif choose==2:
        os.system('clear')
        delete_book_by_id()
    elif choose==3:
        while(True):
            os.system('clear')
            find_book_by_name()
            choose=get_number(allRecords_options)
            if choose==1:
                break
    elif choose==4:
        while(True):
            os.system('clear')
            find_book_by_second_name()
            choose=get_number(allRecords_options)
            if choose==1:
                break
    elif choose==5:
        while(True):
            os.system('clear')
            find_book_by_year()
            choose=get_number(allRecords_options)
            if choose==1:
                break
    elif choose==6:
        while(True):
            os.system('clear')
            find_book_by_title()
            choose=get_number(allRecords_options)
            if choose==1:
                break
    elif choose==7:
        while(True):
            os.system('clear')
            getAllRecords()
            choose=get_number(allRecords_options)
            if choose==1:
                break
    elif choose==8:
        break