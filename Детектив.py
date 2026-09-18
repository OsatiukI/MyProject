import random
things_in_the_room = ["письменный стол","кресло","книжный шкаф", "сейф", "камин", "картина", "часы", "ваза", "ковёр", "окно", "дверь", "разбитый стакан", "окровавленный носовой платок", "следы грязи на полу" ]
room_items = {
    "письменный стол": {
        "description": "Стол выглядит целым, ничего подозрительного нет"
    },
    "кресло": {
        "description": "На кресле лежит шарф служанки"
    },
    "книжный шкаф":{
        "description": "Старые книги покрыты пылью"
    },
    "сейф": {
        "description": "Сейф закрыт"
    },
    "камин": {
        "description": "Слегка теплые угли говорят о том, что со вчера камин не топили"
    },
    "картина": {
        "description": "Нарисован дикий табун лошадей"
    },
    "часы": {
        "description": "Часы остановились на 8 45"
    },
    "ваза": {
        "description": "На вазе есть скол и слегка заметные пятна еще свежей крови"
    },
    "ковёр": {
        "description": "На ковре лежит осколок от вазы"
    },
    "окно":{
        "description": "Окно чистое, такое чувство что его недовно помыли"
    },
    "дверь":{
        "description": "Дверь без признаков взлома"
    },
    "разбитый стакан": {
        "description": "Явный запах виски присудствует на осколках стакана"
    },
    "окровавленный носовой платок": {
        "description": ""
    },
    "следы грязи на полу": {
        "description": "Явные пятна грази, но тяжело сказать от куда она. Последнюю неделю идут дожди"
    }
}
suspects = {
    "мария" : {
        "role": "Служанка",
        "alibi": "Убиралась на кухне",
        "description": "Немного нервничает"
    },
    "игорь": {
        "role": "Племяник",
        "alibi": "Читал книгу в гостиной",
        "description": "Ведёт себя спокойно"
    },
    "виктор": {
        "role": "Охраник",
        "alibi": "Патрулировал территорию снаружи",
        "description": "Уверено отвечает на вопросы"
    },
    "елена": {
        "role": "Гостья",
        "alibi": "Разговаривала по телефону на террасе",
        "description": "Избегает зрительного контакта"
    }
}
def examine_room(room_items):
        print("В комнате вы нашли: ")
        for item in room_items :
            print(item)

def show_room_items(room_items):
        print("Вы иследуюете: ")
        item = input().lower()
        if item in room_items:
            print(room_items[item]["description"])
        else:
            print("Такой улики нет!")

def grew_up(suspects):
         print("Кого ты хочешь допросить?")
         for suspect in suspects :
            print(suspect)
         suspect = input("Скажи кого вызвать на допрос?: ").lower()
         if suspect in suspects:
             print("Кто ты? Я", suspects[suspect]["role"])
             print("Где ты был в момент нападения? Я", suspects[suspect]["alibi"])
             print("Поведение подозреваемого: ", suspects[suspect]["description"])
         else:
             print("Такого подозреваемого нет!")

def who_thief(suspects):
    print("Кто виновен?")
    suspect = input("Твой выбор: ").lower()

    if suspect == "виктор":
        print("Ты нашел вора")
        return True
    else:
        print("Это не он!")
        return False






print("Добро пожаловать в детективную историю!")
print()
print("Вы — частный детектив, прибывший в старинный особняк.")
print("Знаменитый коллекционер Александр Воронцов найден без сознания.")
print("Событие произошло в 23:00.")
print("Из его коллекции исчез редкий золотой медальон.")
print()
print("В особняке находятся четыре подозреваемых.")
print("Ваша задача — осмотреть комнату, собрать улики,")
print("допросить подозреваемых и найти виновного.")
print()
print("Будьте внимательны: не каждому можно доверять...")
print()


while True:
    print("1. Осмотреть комнату")
    print("2. Посмотреть найденные улики")
    print("3. Допросить подозреваемого")
    print("4. Обвинить подозреваемого")
    print("5. Выйти")
    try:
       answer = int(input("Выберите действие: "))
    except ValueError:
       print("Ошибка!")
       continue
    if answer == 1:
       examine_room(room_items)
    elif answer == 2:
        show_room_items(room_items)
    elif answer == 3:
        grew_up(suspects)
    elif answer == 4:
        result = who_thief(suspects)
        if result == False:
            continue
        else:
            break
    else:
        break
