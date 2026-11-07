import os # стандартный модуль Python для взаимодействия с операционной системой
import asyncio   #стандартная библиотека Python для асинхронного программирования
from pathlib import Path   #класс из стандартного модуля pathlib.Он предназначен для работы с путями к файлам и папкам.
from datetime import datetime   #класс для работы с датами и временем
from dotenv import load_dotenv   #Она загружает переменные из файла .env.
from aiogram import Bot, Dispatcher  #сторонняя библиотека Python для создания Telegram-ботов.
from aiogram.filters import CommandStart, Command   # ыильтры команд
from aiogram.types import Message, BotCommand  #BotCommand — объект, описывающий команду, которую мы хотим добавить в меню Telegram
from database import Database  #Это уже импорт из нашего собственного проекта
from person import Person  #Подключаем класс Person из нашего файла person.py


# Загружаем токен из файла .env
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(env_path, override=True)

TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise ValueError(
        "Не удалось загрузить TELEGRAM_TOKEN. "
        "Проверь файл .env"
    )


# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Подключаем базу данных
database = Database()

# Временное хранилище данных пользователей
user_data = {}


# Команда start
@dp.message(CommandStart())
async def start(message: Message):   # асинхронная фкнкция
    await message.answer(
        "Привет! Я бот для управления базой данных людей.\n\n"
        "Используй /help, чтобы узнать мои возможности."
    )


# Команда help
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Доступные команды:\n\n"
        "/start — запуск бота\n"
        "/help — помощь\n"
        "/people — показать всех людей\n"
        "/search — поиск человека\n"
        "/add — добавить нового человека\n"
        "/cancel — отменить добавление"
    )


# Формирование карточки человека
def format_person(person):
    person_id = person[0]
    first_name = person[1]
    last_name = person[2] or ""
    middle_name = person[3] or ""
    birth_date = person[4]

    full_name = " ".join(
        part for part in
        [last_name, first_name, middle_name]
        if part
    )

    return (
        f"ID: {person_id}\n"
        f"Имя: {full_name}\n"
        f"Дата рождения: {birth_date}\n\n"
    )


# Команда people
@dp.message(Command("people"))
async def show_people(message: Message):
    persons = database.get_all_persons()
    if not persons:
        await message.answer("В базе данных пока нет людей.")
        return
    response = "Список людей:\n\n"
    for person in persons:
        response += format_person(person)
    for i in range(0, len(response), 4000):
        await message.answer(response[i:i + 4000])


# Команда search
@dp.message(Command("search"))
async def search_people(message: Message):
    search_text = message.text.replace("/search", "", 1).strip()
    if not search_text:
        await message.answer(
            "Укажи имя или фамилию для поиска.\n"
            "Например: /search Иван"
        )
        return
    persons = database.search_person(search_text)
    if not persons:
        await message.answer("Ничего не найдено.")
        return
    response = "Результаты поиска:\n\n"
    for person in persons:
        response += format_person(person)
    for i in range(0, len(response), 4000):
        await message.answer(response[i:i + 4000])


# Команда add
@dp.message(Command("add"))
async def add_person_start(message: Message):
    user_id = message.from_user.id
    user_data[user_id] = {
        "step": "first_name"
    }
    await message.answer(
        "Добавление нового человека.\n\n"
        "Введи имя:"
    )


# Команда cancel
@dp.message(Command("cancel"))
async def cancel_add(message: Message):
    user_id = message.from_user.id
    if user_id in user_data:
        user_data.pop(user_id)
        await message.answer("Добавление отменено.")
    else:
        await message.answer("Сейчас нет активного добавления.")


# Обработка ответов при добавлении человека
@dp.message()
async def add_person_dialog(message: Message):
    user_id = message.from_user.id
    if user_id not in user_data:
        return
    if not message.text:
        await message.answer("Пожалуйста, отправь текстовый ответ.")
        return
    answer = message.text.strip()
    step = user_data[user_id]["step"]
    if step == "first_name":
        if not answer:
            await message.answer("Имя не может быть пустым. Введи имя:")
            return
        user_data[user_id]["first_name"] = answer
        user_data[user_id]["step"] = "last_name"
        await message.answer(
            "Введи фамилию (если нет, напиши -):"
        )

    elif step == "last_name":
        user_data[user_id]["last_name"] = (
            None if answer == "-" else answer
        )
        user_data[user_id]["step"] = "middle_name"
        await message.answer(
            "Введи отчество (если нет, напиши -):"
        )

    elif step == "middle_name":
        user_data[user_id]["middle_name"] = (
            None if answer == "-" else answer
        )
        user_data[user_id]["step"] = "birth_date"
        await message.answer(
            "Введи дату рождения в формате ДД.ММ.ГГГГ:"
        )

    elif step == "birth_date":
        try:
            birth_date = datetime.strptime(
                answer, "%d.%m.%Y"
            ).date()
        except ValueError:
            await message.answer(
                "Неверная дата.\n"
                "Попробуй ещё раз: ДД.ММ.ГГГГ"
            )
            return
        user_data[user_id]["birth_date"] = birth_date
        user_data[user_id]["step"] = "death_date"
        await message.answer(
            "Введи дату смерти в формате ДД.ММ.ГГГГ.\n"
            "Если человек жив, напиши -:"
        )

    elif step == "death_date":
        if answer == "-":
            death_date = None
        else:
            try:
                death_date = datetime.strptime(
                    answer, "%d.%m.%Y"
                ).date()
            except ValueError:
                await message.answer(
                    "Неверная дата.\n"
                    "Попробуй ещё раз: ДД.ММ.ГГГГ"
                )
                return

            if death_date < user_data[user_id]["birth_date"]:
                await message.answer(
                    "Дата смерти не может быть раньше даты рождения. "
                    "Введи дату ещё раз:"
                )
                return
        user_data[user_id]["death_date"] = death_date
        user_data[user_id]["step"] = "gender"
        await message.answer(
            "Укажи пол:\n"
            "М — мужской\n"
            "Ж — женский"
        )

    elif step == "gender":
        gender_value = answer.casefold()

        if gender_value in ("м", "мужской", "m", "male"):
            gender = "m"
        elif gender_value in ("ж", "женский", "f", "female"):
            gender = "f"
        else:
            await message.answer(
                "Не понял пол. Введи М или Ж:"
            )
            return

        try:
            person = Person(
                first_name=user_data[user_id]["first_name"],
                last_name=user_data[user_id]["last_name"],
                middle_name=user_data[user_id]["middle_name"],
                birth_date=user_data[user_id]["birth_date"],
                death_date=user_data[user_id]["death_date"],
                gender=gender
            )

            database.add_person(person)

            await message.answer(
                "Человек успешно добавлен в базу данных!"
            )

        except (ValueError, TypeError) as error:
            await message.answer(
                f"Не удалось добавить человека: {error}"
            )

        except Exception as error:
            print(f"Ошибка базы данных: {error}")
            await message.answer(
                "Произошла ошибка при сохранении в базу данных."
            )

        finally:
            user_data.pop(user_id, None)


# Запуск бота
async def main():
    await bot.set_my_commands([
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="help", description="Помощь"),
        BotCommand(command="people", description="Показать всех людей"),
        BotCommand(command="search", description="Найти человека"),
        BotCommand(command="add", description="Добавить человека"),
        BotCommand(command="cancel", description="Отменить добавление")
    ])

    print("Telegram-бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    finally:
        asyncio.run(bot.session.close())
