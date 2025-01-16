#Просмотр списка книг
def book_list_view(library):
    if library:
        for book in library:
            print(f"{book}: {library[book]["availability"]}")
    else:
        print("В библиотеке нет книг!")


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
    if title in library and library[title]["availability"] is True \
        or library[title]["availability"] == None:
        library[title]["availability"] = False
        print("Книга успешно выдана!")
    elif library[title]["availability"] is False:
        print("Книга уже выдана!")
    else:
        print("Такой книги нет в библиотеке!")


#Функция возврата книги
def return_book(title):
    if title in library and library[title]["availability"] is False:
        library[title]["availability"] = True
        print("Книгу вернули в библиотеку!")
    elif library[title]["availability"] is True:
        print("Книга уже в библиотеке!")
    else:
        print("Такой книги нет в библиотеке!")


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
add_book("Три мушкетера", "Александр Дюма", 1890) #Добавили книгу
remove_book("Война миров") #Удалили книгу
issue_book("Три мушкетера") #Забрали книгу
return_book("Три мушкетера") #Вернули книгу
find_book("Война и мир") #Поиск книги
