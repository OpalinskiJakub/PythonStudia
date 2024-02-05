class Book:
    def __init__(self, book_id, title, author_first_name, author_last_name, publication_year):
        self.book_id = book_id
        self.title = title
        self.author_first_name = author_first_name
        self.author_last_name = author_last_name
        self.publication_year = publication_year

# Sample data
books = [
    Book(1, "To Kill a Mockingbird", "Harper", "Lee", 1960),
    Book(2, "1984", "George", "Orwell", 1949),
    Book(3, "The Great Gatsby", "F. Scott", "Fitzgerald", 1925),
]

def print_books_terminal(books):
    # Calculate column widths
    book_id_width = max(len("Book ID"), max(len(str(book.book_id)) for book in books)) + 2
    title_width = max(len("Title"), max(len(book.title) for book in books)) + 2
    author_fn_width = max(len("Author First Name"), max(len(book.author_first_name) for book in books)) + 2
    author_ln_width = max(len("Author Last Name"), max(len(book.author_last_name) for book in books)) + 2
    pub_year_width = max(len("Publication Year"), max(len(str(book.publication_year)) for book in books)) + 2

    # Print the header
    header = f"| {'Book ID':<{book_id_width}} | {'Title':<{title_width}} | {'Author First Name':<{author_fn_width}} | {'Author Last Name':<{author_ln_width}} | {'Publication Year':<{pub_year_width}} |"
    divider = "-" * len(header)
    print(divider)
    print(header)
    print(divider)

    # Print each book record
    for book in books:
        print(f"| {book.book_id:<{book_id_width}} | {book.title:<{title_width}} | {book.author_first_name:<{author_fn_width}} | {book.author_last_name:<{author_ln_width}} | {book.publication_year:<{pub_year_width}} |")
    print(divider)

# Display the books in the refined terminal-friendly format
print_books_terminal(books)
