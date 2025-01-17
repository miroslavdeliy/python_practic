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
    if title in library and library[title]["availability"] is not False:
        library[title]["availability"] = False
        print("Книга успешно выдана!")
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
        print(f"\n{title}\nАвтор: {library[title]["author"]}\
        \nГод издания: {library[title]["year"]}")
        if library[title]["availability"] == None:
            print ("Наличие: Книга в библиотеке, но ее статус не определен!")
        elif library[title]["availability"] is False:
            print("Наличие: Книга выдана!")
        else:
            print("Наличие: Книга доступна!")
    else:
        print("Такой книги нет в библиотеке!")


def menu():
    check_exit = True
    while check_exit:
        print ("Выберите, номер действия:\n1.Вывести список книг\
           \n2.Добавить или обновить книгу\n3.Удалить книгу\
           \n4.Выдать книгу\n5.Вернуть книгу\n6.Посмотреть информацию о книге\
           \n7.Выход\n")
        try:
            users_choice = int(input())
        except ValueError:
            print("Ошибка! Введите числа из списка!")
            continue
        if users_choice == 1:
            book_list_view(library)
        elif users_choice == 2:
            title = input("Введите название книги: ")
            author = input("Введите автора: ")
            try:
                year = int(input("Введите год издания: "))
            except ValueError:
                print("Ошибка введите год числами!")
                continue
            add_book(title, author, year)
        elif users_choice == 3:
            title = input("Введите название книги: ")
            remove_book(title)
        elif users_choice == 4:
            title = input("Введите название книги: ")
            issue_book(title)
        elif users_choice == 5:
            title = input("Введите название книги: ")
            return_book(title)
        elif users_choice == 6:
            title = input("Введите название книги: ")
            find_book(title)
        elif users_choice == 7:
            check_exit = False
        else:
            print("Введите только пункты из меню!")


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

menu()