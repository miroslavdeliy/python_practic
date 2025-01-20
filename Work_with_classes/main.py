class ToDoList:
    #Конструктор
    def __init__(self):
        self.note = {}

    #Добавить задачу
    def add_task(self, task):
        self.note[task] = 1

    #Выполнить задачу
    def complete_task(self, task):
        if task in self.note:
            self.note[task] = 2
        else:
            print("Такой задачи не существует!")

    #Удалить задачу
    def remove_task(self, task):
        if task in self.note:
           del self.note[task]
        else:
            print("Такой задачи не существует!")

    #Вывести список задач
    def list_tasks(self):
        print("Список задач. 1 - не выполнено; 2 - выполнено")
        for task in self.note:
            print(f"{task}: {self.note[task]}")


todo = ToDoList()
check_exit = True
while check_exit:
    print("Выберите номер действия:\n1. Добавить задачу\
          \n2. Выполнить задачу\n3. Удалить задачу\n4. Вывести список задач\
          \n5. Выход")
    user_choice = input()
    if user_choice == "1":
        todo.add_task(input("Введите задачу! "))
    elif user_choice == "2":
        todo.complete_task(input("Введите задачу для выполнения "))
    elif user_choice == "3":
        todo.remove_task(input("Введите задачу для удаления "))
    elif user_choice == "4":
        todo.list_tasks()
    elif user_choice == "5":
        check_exit = False
    else:
        print("Вводите только пункты из меню!")

