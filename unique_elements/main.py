#Функция создания списка
def enter_list():
    my_list = []
    check_exit = True
    while check_exit:
        my_list.append(input("Введите элемент списка: "))
        check_enter = input("Хотите продолжить? Y/N ").upper()
        if check_enter == "Y":
            check_exit = True
        elif check_enter == "N":
            check_exit = False
        else:
            print("Ошибка! Введите Y или N")
    return my_list


print("Количество уникальных элементов: ", len(set(enter_list())))



