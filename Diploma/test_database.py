from database import Database
from person import Person


def check(description, condition):
    if condition:
        print(f"[OK] {description}")
    else:
        raise AssertionError(f"[ОШИБКА] {description}")


# Используем отдельную тестовую базу
db = Database("test_people.db")

# Создаём таблицу
db.create_table()

# Очищаем предыдущие тестовые записи
connection = db.connect()
connection.execute("DELETE FROM people")
connection.commit()
connection.close()

print("\n--- НАЧАЛО ПРОВЕРКИ ---\n")


# 1. Создаём двух человек
ivan = Person(
    first_name="Иван",
    last_name="Иванов",
    middle_name="Иванович",
    birth_date="12.10.1990",
    gender="m"
)

anna = Person(
    first_name="Анна",
    last_name="Петрова",
    birth_date="15.05.1995",
    gender="f"
)

print("1. Проверка добавления")

db.add_person(ivan)
db.add_person(anna)

people = db.get_all_persons()

check("Добавление двух человек", len(people) == 2)


# 2. Проверяем получение всех записей
print("\n2. Проверка получения записей")

check("Получение всех записей", len(db.get_all_persons()) == 2)


# 3. Проверяем поиск
print("\n3. Проверка поиска")

results = db.search_person("иван")
print("Результат поиска:", results)
print("Количество найденных записей:", len(results))

check("Поиск без учёта регистра", len(results) == 1)
check("Найден правильный человек", results[0][1] == "Иван")


# 4. Проверяем редактирование
print("\n4. Проверка редактирования")

ivan_id = results[0][0]

updated_ivan = Person(
    first_name="Иван",
    last_name="Сидоров",
    middle_name="Иванович",
    birth_date="12.10.1990",
    gender="m"
)

db.update_person(ivan_id, updated_ivan)

updated_results = db.search_person("Сидоров")

check("Редактирование фамилии", len(updated_results) == 1)


# 5. Проверяем удаление
print("\n5. Проверка удаления")

db.delete_person(ivan_id)

remaining_people = db.get_all_persons()

check("Удаление человека", len(remaining_people) == 1)
check("Анна осталась в базе", remaining_people[0][1] == "Анна")


print("\n--- ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ ---")