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
    "меч": {"damage": 20, "critical_hit_chance": 10, "miss_chance": 5, "durability": 100},
    "топор": {"damage": 25, "critical_hit_chance": 2, "miss_chance": 15, "durability": 100},
    "посох": {"damage": 27, "critical_hit_chance": 7, "miss_chance": 8, "durability": 100},
    "булава": {"damage": 30, "critical_hit_chance": 3, "miss_chance": 15, "durability": 100},
    "лук": {"damage": 35, "critical_hit_chance": 20, "miss_chance": 30, "durability": 100},
}
monsters_data = {
    "волк": {"health": 50, "damage": 10, "xp": 5, "gold": 10, "miss_chance": 5, "critical_hit_chance_m": 20},
    "гоблин": {"health": 60, "damage": 15, "xp": 10, "gold": 15, "miss_chance": 7, "critical_hit_chance_m": 15},
    "дракон": {"health": 90, "damage": 25, "xp": 20, "gold": 50, "miss_chance": 30, "critical_hit_chance_m": 5},
    "трупоед": {"health": 80, "damage": 17, "xp": 15, "gold": 40, "miss_chance": 10, "critical_hit_chance_m": 10},
    "кикимора": {"health": 85, "damage": 20, "xp": 15, "gold": 30, "miss_chance": 15, "critical_hit_chance_m": 12}
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
    #print("прочность:" f"{weapons[player['weapon']]['durability']} из 100",)
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
        monster_gold = monster_stats["gold"]
        while True:
            if player["weapon"] == None:
                player_damage = 5
            else:
                miss_chance = weapons[player["weapon"]]["miss_chance"]

                if random.randint(1, 100) <= miss_chance:
                    player_damage = 0
                    print("Промах!")
                else:
                    base_damage = weapons[player["weapon"]]["damage"]
                    player_damage = random.randint(int(base_damage * 0.8), base_damage)
                    weapons[player["weapon"]]["durability"] -= random.randint(1, 5)
                    #crash_weapon = crash_weapons - random.randint(1, 5)
                    if weapons[player["weapon"]]["durability"] <= 0:
                        player["inventory"].remove(player["weapon"])
                        player["weapon"] = None
                        print("Оружие сломалось: ")
                        continue
                        #print("Оружие сломалось: ")

                    else:
                        print("Прочность оружия: ", weapons[player["weapon"]]["durability"])

                    critical_chance = weapons[player["weapon"]]["critical_hit_chance"]

                    if random.randint(1, 100) <= critical_chance:
                        player_damage *= 2
                        print("Критический удар!")

            monster_health -= player_damage
            print("Вы атаковали: ", player_damage)
            print("Здоровье монстра: ", monster_health)
            if monster_health <= 0:
                print("Монстер отправился в Валхалу")
                break
            else:
                miss_chance_m = monsters_data[monster]["miss_chance"]
                if random.randint(1, 100) <= miss_chance_m:
                      print("Монстр промахнулся")
                      damage_taken = 0
                else:
                    base_damage_m = monsters_data[monster]["damage"]
                    monster_damage = random.randint(int(base_damage_m * 0.8), base_damage_m)
                    critical_chance_m = monsters_data[monster]["critical_hit_chance_m"]
                    if random.randint(1, 100) <= critical_chance_m:
                        monster_damage *= 2
                        print("Критический удар!", monster_damage)
                    damage_taken = max(0, monster_damage - player_defense)


                player["health"] -= damage_taken
                print("Атака монстра: ", damage_taken)
                print("Ваше здоровье: ", player["health"], "Защита брони: ", player_defense)
                if player["health"] <= 0:
                   print("Смерть :(")
                   return False



        add_gold(player, monster_gold)
        add_xp(player, monster_xp)
        print("Вы победили монстра")
        print("Вы получили" , monster_gold , "золота")
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

def blacksmit(player):
    print("Добро пожаловать в мою кузницу, странник!")
    print("Принеси своё оружие — я осмотрю его и скажу, сколько будет стоить ремонт.")
    print("Если цена тебя устроит — верну твоему оружию прежнюю прочность!")
    if player["weapon"] == None:
        print("Оружие не выбрано")
    else:
       repair_weapon_price = round((100 - weapons[player["weapon"]]["durability"]) * 0.3)
       if player["gold"] < repair_weapon_price:
         print("Незватает золота!")

       else:
           print("Ремонт вашего оружия будет стоить ", repair_weapon_price,"золота. Согласны?")
           print("Да или Нет")
           answer = input("Ваше рещение: ").lower()
           if answer == "да":
               player["gold"] -= repair_weapon_price
               weapons[player["weapon"]]["durability"] = 100
               print("Вы потратили ", repair_weapon_price, "на ремонт")
               print("Прочность оружия: ", weapons[player["weapon"]]["durability"])
           elif answer == "нет":
                return
           else:
               print("Такой выбор не допустим")
               return









while True:
    print("1. Показать персонажа:")
    print("2. Показать магазин: ")
    print("3. Купить предмет: ")
    print("4. Продать предмет: ")
    print("5. Пройти квест: ")
    print("6. Использовать предмет: ")
    print("7. Кузнец")
    print("8. Выйти")
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
        blacksmit(player1)
    elif answer == 8:
        break
    else:
        print("Такого дествия нет!")





