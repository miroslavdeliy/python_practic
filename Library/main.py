#Просмотр списка книг
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
    if title in library and library[title]["availability"] == True:
        library[title]["availability"] = False
        print("Книга успешно выдана!")
    else:
        print("Такой книги нет в библиотеке!")


#Функция возврата книги
def return_book(title):
    if title in library:
        library[title]["availability"] = True
        print("Книгу успешно вернули!")
    else:
        print("Такой книги нет в наличии!")


#Функция поиска книги
def find_book(title):
    if title in library:
        print(f"{title}: Автор: {library[title]["author"]},\
        Год издания: {library[title]["year"]}, Наличие в библиотеке:\
        {library[title]["availability"]}")
    else:
        print("Такой книги нет в библиотеке!")


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
print("Обновленный список книг в библиотеке:")
book_list_view(library)
return_book("Война и мир")#Вернули книгу
print("Обновленный список книг в библиотеке:")
book_list_view(library)
find_book("Война и мир")#Поиск книги
