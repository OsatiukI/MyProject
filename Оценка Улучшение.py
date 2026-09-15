grades = []
def show_grades():
    for number, item in enumerate(grades, 1):
        print(str(number) + ".", item)
def average_grades():
    if not grades:
        print("Еще нет оценок")
    else:
        answermid = sum(grades) / len(grades)
        print("Ваша средняя оценка:", answermid)
def max_grades():
    if not grades:
        print("Еще нет оценок!")
    else:
        answermax = max(grades)
        print("Ваша лучшая оценка: ", answermax)


while True:
    print("1 — Добавить оценку")
    print("2 — Показать оценки")
    print("3 — Показать среднюю оценку")
    print("4 — Показать лучшую оценку")
    print("5 — Выйти")
    answer = int(input("Выбери действие: "))
    if answer == 1:
        while True:
            item = int(input("Введите оценку: "))
            if item == 0:
                break
            else:
                grades.append(item)
    elif answer == 2:
         show_grades()

    elif answer == 3:
        average_grades()

    elif answer == 4:
        max_grades()

    elif answer == 5:
        break
    else:
        print("Такого значения нет!")





