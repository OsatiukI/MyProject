inventory = []
def add_item(inventory):
    item = str(input("Введите название предмета: ")).lower()
    inventory.append(item)
def show_items(inventory):
    for nubmer, item in enumerate(inventory, 1):
        print(str(nubmer) + ". " + item)
def del_item(inventory):
    n_number = int(input("Ввкдите номер предмета: "))
    del inventory[n_number - 1]
def find_item(inventory):
    fitem = str(input("Ввкдите что ищете: ")).lower()
    if fitem in inventory:
        print("Предмет найден: " + fitem)
    else:
        print("Такого предмета нет", fitem)
def count_items(inventory):
    count = len(inventory)
    print(("Количество предметов: " +str(count)))
while True:
    print("1 - Добавить предмет: ")
    print("2 - Показать инвентарь: ")
    print("3 - Удалить предмет: ")
    print("4 - Найти предмет: ")
    print("5 - Количество пркдметов: ")
    print("6 - Выйти")
    answer = int(input("Введите свой выбор: "))
    if answer == 1:
        add_item(inventory)
    elif answer == 2:
        show_items(inventory)
    elif answer == 3:
        del_item(inventory)
    elif answer == 4:
        find_item(inventory)
    elif answer == 5:
        count_items(inventory)
    elif answer == 6:
        break


