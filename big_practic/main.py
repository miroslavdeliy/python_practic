from statistics import mean

#Расчет среднего
def calculate_average(grades):
    if grades:
        return round(mean(grades),2)
    else:
        print("Список пустой!")


#Пересчет списка студентов
def calculation(dict_average, students):
    for student in students:
        average_grade = calculate_average(student["grades"])
        dict_average[student["name"]] = average_grade


#Вывод информации о студентах
def output_information():
    for key, value in dict_average.items():
        if value <= 75:
            status = "Неуспешен"
        else:
            status = "Успешен"
        print(f"Студент: {key}\nСредний балл: {value}\nСтатус: {status}\n")
    print(f"Общий средний балл группы: {group_average()}")


#Общий средний балл группы
def group_average():
    average = dict_average.values()
    return calculate_average(average)


#Добавление студента
def add_student(name, grades, students, dict_average):
    students.append({"name": name, "grades": grades})
    print("Студент добавлен!")
    dict_average[name] = calculate_average(grades)
    output_information()


#Удаление неуспевающего студента
def delete_student(students, dict_average):
    min_average = min(dict_average.values())
    for name in dict_average:
        if dict_average[name] == min_average:
            students_name = name
            del dict_average[name]
            break
    for student in students:
        if student["name"] == students_name:
            students.remove(student)
            print("Студент удален!")
            break
    output_information()


students = [
    {"name": "Harry", "grades": [80,90,78]},
    {"name": "Hermione", "grades": [95,90,97]},
    {"name": "Ron", "grades": [60,70,64]},
    {"name": "Draco", "grades": [60,75,70]}
]
dict_average = {}

calculation(dict_average, students)
output_information()
add_student("Dambldore", [90, 60, 90],students, dict_average)
delete_student(students,dict_average)