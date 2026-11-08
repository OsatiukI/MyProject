classes = {
    "Warrior":{"health": 100,"damage": 5,"level": 1,},
    "Mage":{"health": 120,"damage": 10,"level": 1,},
    "Archer":{"health": 150,"damage": 5,"level": 1,}
}
for class_name in classes:
    print(class_name)
name = input("Выбери имя: ")
choice = input("Выбери класс: ")
if choice in classes:
    stats = classes[choice]
    print("Имя: ", name)
    print("Здоровье", stats["health"])
    print("Урон", stats["damage"])
    print("Уровень", stats["level"])
else:
   print("error")












