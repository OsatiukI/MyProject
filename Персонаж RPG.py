import random
monsters = ["волк", "гоблин", "дракон", "трупоед", "кикимора"]

player1 = {
    "name": "Воин",
    "level": 1,
    "health": 100,
    "gold": 150,
    "weapon": "Меч",
    "inventory": ["меч", "щит", "лук"]
}
shop = {
    "зелье": 30,
    "большое зелье": 60,
    "меч": 100,
    "щит": 80,
    "лук": 70,
    "топор": 120,
    "посох": 90,
    "шлем": 75,
    "броня": 200
}
def show_shop(shop):
    for item, price in shop.items():
        print(item, "-", price, "золота")


def show_player(player):
    print("Имя:", player["name"])
    print("Уровень: ", player["level"])
    print("Здоровье: ", player["health"])
    print("Количество золота: ", player["gold"])
    print("Тип оружия: ", player["weapon"])
    print("Инвентарь:")
    for number, item in enumerate(player["inventory"], 1):
        print(number, item)

def add_gold(player, amount):
    player["gold"] += amount
    print("Золото добавлено: ", player["gold"])

def spend_gold(player, amount):
    if player["gold"] >= amount:
        player["gold"] -= amount
    else:
        print(" Не хватает денег!")

def buy_item(player, item, shop):
    if item in shop:
        price = shop[item]
        if player["gold"] >= price:
            player["gold"] -= price
            player["inventory"] .append(item)
            print("Предмет: ", item, "успешно добавлен")
        elif player["gold"] < price:
            print("Нехватает золота!")
    else:
        print("Такого предмета нет!")

def sell_item(player, item, shop):
    if item in player["inventory"]:
        price = shop[item] / 2
        player["gold"] += price
        player["inventory"].remove(item)
        print("Предмет :", item, "успешно продан.")
    else:
        print("Такого предмета нет.")

def quest(player):

        print("Вы отпавились в лес")
        monster = random.choice(monsters)
        if monster == "волк":
               damage = 10
        elif monster == "гоблин":
               damage = 15
        elif monster == "дракон":
               damage = 25
        elif monster == "трупоед":
               damage = 17
        else:
               damage = 20
        print("Вы встретили", monster)
        player["health"] -= damage
        if player["health"] <= 0:
            print("Смерть :(")
            return False
        else:
            add_gold(player, 50)
            print("Вы победили монстра")
            print("Вы получили 50 золота")
        print("Вы потеряли", damage, "здоровья")


def use_item(player):
    item = input("Ввкдите предмет: ").lower()
    if item in player["inventory"]:
        if item == "зелье":
            player["health"] = min(100, player["health"] + 20)
            player["inventory"].remove(item)
            print("Вы выпили зелье")
            print("Здоровье: ", player["health"])
        elif item != "зелье":
            print("Нельзя использовать!")


    else:
            print("Такого нет")





while True:
    print("1. Показать персонажа:")
    print("2. Показать магазин: ")
    print("3. Купить предмет: ")
    print("4. Продать предмет: ")
    print("5. Пройти квест: ")
    print("6. Исаользовать предмет: ")
    print("7. Выйти")
    answer = int(input("Выберите действие: "))
    if answer == 1:
        show_player(player1)
    elif answer == 2:
        show_shop(shop)
    elif answer == 3:
        item = input("Какой предмет хочешь купить? ").lower()
        buy_item(player1, item, shop)
    elif answer == 4:
        item = input("Какой предмет продать? ").lower()
        sell_item(player1, item, shop)
    elif answer == 5:
        result = quest(player1)
        if result == False:
            break
    elif answer == 6:
        use_item(player1)





