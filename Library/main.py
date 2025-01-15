#Просмотр списка книг
from pickle import FALSE


def book_list_view(library):
    for book in library:
        print(f"{book}: {library[book]["availability"]}")


#Добавление или обновление книги
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


#Удаление книги
def remove_book(title):
    if title in library:
        del library[title]
        print("Книга удалилась!")
    else:
        print("Такой книги нет в библиотеке!")


#Функция выдачи книги
def issue_book(title):
    if title in library:
        if library[title]["availability"] == True:
            library[title]["availability"] = False
        else:
            print("Данной книги нет в наличии")
    else:
        print("Такой книги нет в библиотеке!")


#Функция возврата книги
def return_book(title):
    if title in library:
        library[title]["availability"] = True
    else:
        print("Такой книги нет в наличии!")


library = {
    "Война и мир": {
        "author": "Лев Толстой",
        "year": 1865,
        "availability": True
    },
    "Война миров": {
        "author": "Герберт Уэллс",
        "year": 1898,
        "availability": True
    },
    "Игра престолов": {
        "author": "Джордж Мартин",
        "year": 1996,
        "availability": True
    }
}

print("Список книг в библиотеке:")
book_list_view(library)
add_book("Три мушкетера", "Александр Дюма", 1890)
remove_book("Война миров")
issue_book("Война и мир") #Забрали книгу
print("\nОбновленный список книг в библиотеке:")
book_list_view(library)
return_book("Война и мир")#Вернули книгу
print("\nОбновленный список книг в библиотеке:")
book_list_view(library)
