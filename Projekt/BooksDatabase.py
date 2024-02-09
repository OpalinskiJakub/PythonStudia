
from Book import Book


import json

class BooksDatabase:
    def __init__(self, db_path):
        self.db_path = db_path

    def load_database(self):
        try:
            with open(self.db_path, 'r', encoding='utf-8') as file:
                books_data = json.load(file)

                books_list = []
                for book in books_data:
                    book_object = Book(**book)

                    books_list.append(book_object)
                return books_list
        except FileNotFoundError:
            return []

    def save_database(self, books):
        books_list_dicts = []
        for book in books:
            book_attrs = vars(book)
            books_list_dicts.append(book_attrs)

        with open(self.db_path, 'w', encoding='utf-8') as file:
            json.dump(books_list_dicts, file, ensure_ascii=False, indent=4)


    def get_next_id(self):
        books = self.load_database()
        max_id = 0
        for book in books:
            if book.book_id > max_id:
                max_id = book.book_id
        return max_id + 1


    def insert_book(self, title, author_first_name, author_last_name, publication_year):
        new_id = self.get_next_id()
        new_book = Book(new_id, title, author_first_name, author_last_name, publication_year)
        db = self.load_database()
        db.append(new_book)
        self.save_database(db)

    def delete_book(self, book_id):
        db = self.load_database()
        updated_books = []
        for book in db:
            if book.book_id != book_id:
                updated_books.append(book)
        self.save_database(updated_books)

    def find_book_by_author_first_name(self, first_name):
        db = self.load_database()
        matching_books = []
        for book in db:
            if book.author_first_name.lower() == first_name.lower():
                matching_books.append(book)
        return matching_books

    def find_book_by_author_last_name(self, last_name):
        db = self.load_database()
        matching_books = []
        for book in db:
            if book.author_last_name.lower() == last_name.lower():
                matching_books.append(book)
        return matching_books

    def find_book_by_year(self, year):
        db = self.load_database()
        matching_books = []
        for book in db:
            if int(book.publication_year) == int(year):
                matching_books.append(book)
        return matching_books

    def find_book_by_title(self, title):
        db = self.load_database()
        matching_books = []
        for book in db:
            if title.lower() in book.title.lower():
                matching_books.append(book)
        return matching_books


    def list_books(self):
        db = self.load_database()
        return db
