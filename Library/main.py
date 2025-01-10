def book_list_view(library):
    for book in library:
        print(f"{book}: {library[book]["availability"]}")


library = {
    "Война и мир": {
        "author": "Лев Толстой",
        "year": 1865,
        "availability": "есть"
    },
    "Война миров": {
        "author": "Герберт Уэллс",
        "year": 1898,
        "availability": "есть"
    },
    "Игра престолов": {
        "author": "Джордж Мартин",
        "year": 1996,
        "availability": "нет"
    }
}

print("Список книг в библиотеке:")
book_list_view(library)