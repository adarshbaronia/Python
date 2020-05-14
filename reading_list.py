reading_list = []
menu_prompt = """ Please enter one of the following options:
-'a' to add a book
-'l' to list the book
-'q' to quit

What would you like to do?
"""
selected_option = input(menu_prompt).strip().lower()


def add_book():
    title = input("Title: ").strip().title()
    author = input("Author: ").strip().title()
    year = input("Year of publication: ").strip()

    with open("books.csv", "a") as reading_list:
        reading_list.write(f"{title}, {author}, {year}\n")


def get_all_books():
    books = []

    with open("books.csv", "r") as reading_list:
        for book in reading_list:
            title, author, year = book.strip().split(",")

            books.append({
                "title": title,
                "author": author,
                "year": year
            })
    return books


def show_book(books):
    print()

    for book in books:
        title, author, year = book.values()
        print(f"{title}, by {author} {year}")

    print()


while selected_option != 'q':
    if selected_option == 'a':
        add_book()
    elif selected_option == 'l':
        reading_list = get_all_books()
        if reading_list:
            show_book(reading_list)
        else:
            print("Please add a book.")
        print()
    else:
        print(f"sorry, '{selected_option}' isn't a valid option.")
    print()

    selected_option = input(menu_prompt).strip().lower()
