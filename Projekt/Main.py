from BooksDatabase import BooksDatabase


db = BooksDatabase('books_database.json')


#db.insert_book('The Great Gatsby', 'F. Scott', 'Fitzgerald', 1925)
#db.insert_book('To Kill a Mockingbird', 'Harper', 'Lee', 1960)


print("Listowanie wszystkich książek:")
#db.list_books()

print(db.find_book_by_author_first_name("Harper")[0].title)