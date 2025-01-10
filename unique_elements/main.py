#Функция создания списка
def enter_list():
    my_list = []
    while True:
        symbol = input("Введите элемент списка или Enter, чтобы закончить ")
        #Если пользователь нажал пробел, то выход из цикла
        if symbol == '':
            break
        else:
            my_list.append(symbol)
    return my_list


print("Количество уникальных элементов: ", len(set(enter_list())))



