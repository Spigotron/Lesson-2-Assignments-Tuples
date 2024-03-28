library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def new_book():
    title = input("Please enter the title of the book. ")
    if any(book[0] == title for book in library):
        print("Sorry, that book's already in the library. No duplicates allowed!")
    else:
        author = input("Please enter the author of the book. ")
        added_book = title, author
        library.append(added_book)
        print("Book successfully added to library!")
        print(library)

new_book()