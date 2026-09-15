shopping = []
while True:
    print("1 - Добавить товар:")
    print("2 - Показать список:")
    print("3 - Удалить товар:")
    print("4 - Выйти")
    answer = int(input("Выберете действие: "))
    if answer == 1:
        while True:
           item = input("Введи товар: ") .lower()
           if item == "стоп" .lower():
             break
           else:
             shopping.append(item)

    elif answer == 2:
        for number, item in enumerate(shopping, 1):
            print(number, item)


    elif answer == 3:
        number = int(input("Введи номер продукта: "))
        del shopping[number - 1]
        print("Список продуктов: ")
        for number, item in enumerate(shopping, 1):
            print(number, item)
    elif answer == 4:
        break

    else:
        print("Такого значения нет")






