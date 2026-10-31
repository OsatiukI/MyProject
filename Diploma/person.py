from datetime import datetime, date


class Person:

    def __init__(self, first_name, birth_date, death_date=None, gender=None):
        self.first_name = self.validate_name(first_name)
        self.last_name = None
        self.middle_name = None
        self.birth_date = self.parse_date(birth_date)
        self.death_date = self.parse_date(death_date)
        self.validate_dates()
        self.gender = self.parse_gender(gender)


    def validate_name(self, first_name):
        if first_name is None or not first_name.strip():
            raise ValueError("Имя обязательно для заполнения")
        return first_name.strip()


    def parse_date(self, value):
        if isinstance(value, datetime):
            return value.date()

        if isinstance(value, date):
            return value

        if value is None:
            return None
        value = value.strip()
        date_formats = [
            "%d.%m.%Y",
            "%d %m %Y",
            "%d/%m/%Y",
            "%d-%m-%Y"
        ]
        for date_format in date_formats:
            try:
                return datetime.strptime(value, date_format).date()
            except ValueError:
                continue
        raise ValueError(
            "Неверный формат даты. Используйте: 12.10.1980, 11 10 2000, 01/02/1995 или 3-9-2007")


    def validate_dates(self):
        if self.birth_date is None:
            raise ValueError("Дата рождения обязательна")

        if self.birth_date > date.today():
            raise ValueError("Дата рождения не может быть в будущем")

        if self.death_date is not None:
            if self.death_date < self.birth_date:
                raise ValueError("Дата смерти не может быть раньше даты рождения")

            if self.death_date > date.today():
                raise ValueError("Дата смерти не может быть в будущем")


    def parse_gender(self, gender):
        if gender is None:
            return None
        gender = gender.strip().lower()
        if gender in ("m", "м", "мужчина"):
            return "m"
        elif gender in ("f", "ж", "женщина"):
            return "f"
        else:
            raise ValueError("Некорректно указан пол. Используйте m/f или мужчина/женщина")


    def calculate_age(self):
        if self.death_date is None:
            end_date = date.today()
        else:
            end_date = self.death_date
        age = end_date.year - self.birth_date.year
        if (end_date.month, end_date.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age