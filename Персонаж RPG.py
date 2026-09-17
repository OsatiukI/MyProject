import random
monsters = ["волк", "гоблин", "дракон", "трупоед", "кикимора"]

player1 = {
    "name": "Воин",
    "level": 1,
    "health": 100,
    "max_health": 100,
    "gold": 150,
    "xp": 0,
    "weapon": None,
    "inventory": ["меч", "щит", "лук"],
    "armor": None,
}
shop = {
    "зелье": 30,
    "большое зелье": 60,
    "меч": 100,
    "щит": 80,
    "лук": 70,
    "топор": 120,
    "посох": 110,
    "шлем": 75,
    "броня": 200,
    "булава": 150
}
weapons = {
    "меч": 50,
    "топор": 60,
    "посох": 55,
    "булава": 65,
    "лук": 40,
}
monsters_data = {
    "волк": {"health": 50, "damage": 10, "xp": 5},
    "гоблин": {"health": 60, "damage": 15, "xp": 10},
    "дракон": {"health": 150, "damage": 25, "xp": 20},
    "трупоед": {"health": 100, "damage": 17, "xp": 15},
    "кикимора": {"health": 110, "damage": 20, "xp": 15}
}
armor = {
    "шлем": 10,
    "броня": 50,
    "щит": 15
}
def add_xp(player, amount):
    player["xp"] += amount
    while True:
       if player["xp"] >= 100:
          player["level"] += 1
          player["max_health"] += 20
          player["health"] = player["max_health"]
          print("Новый уровень: ", player["level"])
          player["xp"] -= 100
       elif player["xp"] < 100:
           break

def show_shop(shop):
    for item, price in shop.items():
        print(item, "-", price, "золота")


def show_player(player):
    print("Имя:", player["name"])
    print("Уровень: ", player["level"])
    print("Здоровье: ", player["health"])
    print("Количество золота: ", player["gold"])
    print("Тип оружия: ", player["weapon"])
    print("Броня: ", player["armor"])
    print("Колтчество опыта: ", player["xp"])
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
        if player["armor"] == item:
            player["armor"] = None
    else:
        print("Такого предмета нет.")

def quest(player):

        print("Вы отпавились в лес")
        if player["weapon"] == None:
            player_damage = 5
        else:
            player_damage = weapons[player["weapon"]]
        if player["armor"] == None:
            player_defense = 0
        else:
            player_defense = armor[player["armor"]]
        monster = random.choice(monsters)
        print("Вы встретили", monster)
        monster_stats = monsters_data[monster]
        monster_health = monster_stats["health"]
        monster_damage = monster_stats["damage"]
        monster_xp = monster_stats["xp"]
        while True:
            monster_health -= player_damage
            print("Вы атаковали: ", player_damage)
            print("Здоровье монстра: ", monster_health)

            if monster_health <= 0:
                print("Монстер отправился в Валхалу")
                break
            else:
                damage_taken = max(0, monster_damage - player_defense)
                player["health"] -= damage_taken
                print("Атака монстра: ", monster_damage)
                print("Ваше здоровье: ", player["health"], "Защита брони: ", player_defense)
                if player["health"] <= 0:
                    print("Смерть :(")
                    return False



        add_gold(player, 50)
        add_xp(player, monster_xp)
        print("Вы победили монстра")
        print("Вы получили 50 золота")
        print("Вы получили опты: ", monster_xp)



def use_item(player):
    item = input("Ввкдите предмет: ").lower()
    if item in player["inventory"]:
        if item == "зелье":
            player["health"] = min(player["max_health"], player["health"] + 20)
            player["inventory"].remove(item)
            print("Вы выпили зелье")
            print("Здоровье: ", player["health"])
        elif item == "большое зелье":
            player["health"] = min(player["max_health"], player["health"] + 20)
            player["inventory"].remove(item)
            print("Вы выпили зелье")
            print("Здоровье: ", player["health"])
        elif item in weapons:
            player["weapon"] = item
            print("Экипировано оружие: ", item)
        elif item in armor:
            player["armor"] = item
            print("Экипировано: ", item)

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
    print("6. Использовать предмет: ")
    print("7. Выйти")
    try:
        answer = int(input("Выберите действие: "))
    except ValueError:
        print("Ошибка!")
        continue
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
    elif answer == 7:
        break
    else:
        print("Такого дествия нет!")





