from statistics import mean

#Расчет среднего
def calculate_average(grades):
    return round(mean(grades),2)


#Добавление студента
def add_student(name, grades):
    students.append({"name": name, "grades": grades})
    print("Студент добавлен!")
    recalcultation()


#Удаление неуспевающего студента
def delete_student():
    global min_average
    for student in students:
        if calculate_average(student["grades"]) <= min_average:
            students.remove({"name": student["name"], "grades": student["grades"]})
            print("Студент удален")
    recalcultation()



#Пересчет списка студентов
def recalcultation():
    global min_average
    list_of_average = []
    for student in students:
        average_grade = calculate_average(student["grades"])
        list_of_average.append(average_grade)
        if average_grade >= 75:
            status = "Успешен"
        else:
            status = "Не успешен"
        print(f"Студент {student["name"]}\nСредний балл {average_grade}\
               \nСтатус {status}\n")
    min_average = min(list_of_average)
    print(f"Общий Средний балл потока: {calculate_average(list_of_average)}\n")


students = [
    {"name": "Harry", "grades": [80,90,78]},
    {"name": "Hermione", "grades": [95,90,97]},
    {"name": "Ron", "grades": [60,70,64]},
    {"name": "Draco", "grades": [60,75,70]}
]
min_average = 0
recalcultation()
add_student("Dambldore", [78,89,90])
delete_student()