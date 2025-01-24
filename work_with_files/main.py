def cheсk_correct(func):
    def wrapper(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except FileNotFoundError:
            print("Файл не найден!")
        except PermissionError:
            print("Нет прав доступа к файлу!")
    return wrapper


#Возвращение содержимого файла
@cheсk_correct
def open_for_read(name):
    file = open(name, 'r')
    line = file.read()
    file.close()
    print(line)


#Добавление строки в конец файла
def add_string(name,text):
    file = open(name, 'a')
    file.write(f"\n{text}")
    file.close()


#Чтение построчно
@cheсk_correct
def process_line(name):
    with open(name, 'r') as file:
        for line in file:
            print(line.strip())


#Копирование бинарного файла
@cheсk_correct
def copy_binar_file(name, copy_name):
    with open(name,'rb') as binar_file:
        binar_data = binar_file.read()
    with open(copy_name, 'wb') as binar_file:
        binar_file.write(binar_data)


open_for_read('data.txt')
add_string('data.txt', 'Add new line')
process_line('data.txt')
copy_binar_file('data.txt','copy_data.txt')