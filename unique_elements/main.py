#Функция создания списка
from tabnanny import check


def enter_list():
    my_list = []
    check_exit = True
    while check_exit:
        my_list.append(input("Введите элемент списка: "))
        while True:
            check_enter = input("Хотите продолжить? Y/N ")
            if check_enter == "Y" or check_enter == "y":
                break
            elif check_enter == "N" or check_enter == "n":
                check_exit = False
                break
            else:
                print("Ошибка! Введите Y или N")
                continue
    return my_list


print("Количество уникальных элементов: ", len(set(enter_list())))



