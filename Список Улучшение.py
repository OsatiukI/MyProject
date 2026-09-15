fruts_list = []
def add_fruts(fruts_list):
    fruts = str(input("Введите продукт: "))
    fruts_list.append(fruts)
def show_fruts (fruts_list):
    for number, fruts in enumerate(fruts_list, 1):
        print(str(number) + ".", fruts)
def del_fruts(fruts_list):
    number = int(input("Ввкдите номер фрутка: "))
    del fruts_list[number - 1]
    for number, fruts in enumerate(fruts_list, 1):
        print(number, fruts)
while True:
    print("1 - Добавить продукт: ")
    print("2 - Показать список: ")
    print("3 - Удалить фрукт: ")
    answer = int(input("Выбери действие: "))
    if answer == 1:
       add_fruts(fruts_list)
    elif answer == 2:
        show_fruts(fruts_list)
    elif answer == 3:
        del_fruts(fruts_list)
    else:
        break



