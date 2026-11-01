from database import Database
from interface import Application


def main():
    database = Database()
    database.create_table()

    Application(database)


if __name__ == "__main__":
    main()