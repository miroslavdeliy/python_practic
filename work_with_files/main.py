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
    with open(name, 'r') as file:
        line = file.read()
        print(line)


#Добавление строки в конец файла
def add_string(name,text):
    with open(name, 'a') as file:
        file.write(f"\n{text}")


#Чтение построчно
@cheсk_correct
def process_line(name):
    with open(name, 'r') as file:
        for line in file:
            print(line.strip())


#Копирование бинарного файла
@cheсk_correct
def copy_binary_file(name, copy_name):
    with open(name,'rb') as binary_file:
        binary_data = binary_file.read()
    with open(copy_name, 'wb') as binary_file:
        binary_file.write(binary_data)


open_for_read('data.txt')
add_string('data.txt', 'Add new line')
process_line('data.txt')
copy_binary_file('data.txt','copy_data.txt')