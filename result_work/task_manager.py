import json

class TaskManager:
    #Конструктор класса
    def __init__(self):
        self.task = []

    #Добавление задачи
    def add_task(self,description):
        self.task.append({"description": description, "completed": False})
        print('Задача добавлена!')

    #Отмечает задачу выполненной
    def complete_task(self,index):
        one_task = self.task[index]
        one_task["completed"] = True
        self.task[index] = one_task
        print(f"Задача {one_task["description"]} отмечена выполненной!")

    #Удаляет задачу из списка
    def remove_task(self,index):
        task = self.task.pop(index)
        print(f"Задача {task["description"]} удалена из списка!")

    #Сохранение текущего списка задач в json файл
    def save_to_json(self,filename):
        with open(filename, 'w') as file:
            json.dump(self.task, file, indent=4)
        print(f"Список задач сохранен в файле {filename}!")

    #Загрузка из json в текущий список
    def load_from_json(self, filename):
        with open(filename,'r') as file:
            tasks = json.load(file)
        self.task.extend(tasks)
        print(f"Список задач загружен из файла {filename} в текущий список!")