import sqlite3
from person import Person


class Database:

    def __init__(self, db_name="people.db"):   #Инициализация объекта базы данных
        self.db_name = db_name

    def connect(self):  #Подключение к SQLite
        return sqlite3.connect(self.db_name)


    def create_table(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
              CREATE TABLE IF NOT EXISTS people (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  first_name TEXT NOT NULL,
                  last_name TEXT,
                  middle_name TEXT,
                  birth_date TEXT NOT NULL,
                  death_date TEXT,
                  gender TEXT
              )
          """)
        connection.commit()
        connection.close()


    def add_person(self, person):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO people (
                first_name,
                last_name,
                middle_name,
                birth_date,
                death_date,
                gender
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            person.first_name,
            person.last_name,
            person.middle_name,
            person.birth_date.isoformat(),
            person.death_date.isoformat() if person.death_date else None,
            person.gender
        ))
        connection.commit()
        connection.close()


    def get_all_persons(self):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM people")
        persons = cursor.fetchall()
        connection.close()
        return persons

    def search_person(self, search_text):
        connection = self.connect()
        connection.create_function("CASEFOLD", 1,lambda value: value.casefold() if value else None)
        cursor = connection.cursor()
        search_text = f"%{search_text.casefold()}%"
        cursor.execute("""
            SELECT * FROM people
            WHERE CASEFOLD(first_name) LIKE ?
            OR CASEFOLD(last_name) LIKE ?
            OR CASEFOLD(middle_name) LIKE ?
        """, (search_text, search_text, search_text))
        persons = cursor.fetchall()
        connection.close()
        return persons


    def delete_person(self, person_id):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM people WHERE id = ?", (person_id,))
        connection.commit()
        connection.close()


    def update_person(self, person_id, person):
        connection = self.connect()
        cursor = connection.cursor()
        cursor.execute("""
            UPDATE people
            SET first_name = ?,
            last_name = ?,
            middle_name = ?,
            birth_date = ?,
            death_date = ?,
            gender = ?
            WHERE id = ?
        """, (
            person.first_name,
            person.last_name,
            person.middle_name,
            person.birth_date.isoformat(),
            person.death_date.isoformat() if person.death_date else None,
            person.gender,
            person_id
        ))
        connection.commit()
        connection.close()
