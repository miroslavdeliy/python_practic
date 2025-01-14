def book_list_view(library):
    for book in library:
        print(f"{book}: {library[book]["availability"]}")


def add_book(title, author, year):
    if title in library:
        check_y_n = input("\nДанная книга уже есть. Обновить? Y/N")
        if check_y_n.upper() == "Y":
            library[title] = {
                "author": author,
                "year": year,
                "availability": None
            }
            print("\nКнига обновилась.")
        else:
            print("\nКнига не обновлена!")
    else:
        library[title] = {
            "author": author,
            "year": year,
            "availability": None
        }
        print("\nКнига успешно добавилась!")


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
add_book("Война и мир", "Александр Дюма", 1890)
print("\nОбновленный список книг в библиотеке:")
book_list_view(library)

