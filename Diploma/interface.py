import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from person import Person


class Application:

    def __init__(self, database):
        self.database = database
        self.root = tk.Tk()
        self.root.title("Управление данными о людях")
        self.root.geometry("900x600")
        self.create_table()
        self.load_people()
        self.create_buttons()
        self.root.mainloop()

    def create_table(self):
        columns = (
            "id",
            "first_name",
            "last_name",
            "middle_name",
            "birth_date",
            "death_date",
            "gender"
        )
        self.tree = ttk.Treeview(
            self.root,
            columns=columns,
            show="headings"
        )
        self.tree.heading("id", text="ID")
        self.tree.heading("first_name", text="Имя")
        self.tree.heading("last_name", text="Фамилия")
        self.tree.heading("middle_name", text="Отчество")
        self.tree.heading("birth_date", text="Дата рождения")
        self.tree.heading("death_date", text="Дата смерти")
        self.tree.heading("gender", text="Пол")
        self.tree.pack(fill="both", expand=True)

    def load_people(self):
        persons = self.database.get_all_persons()
        for person in persons:
            self.tree.insert("", "end", values=person)

    def create_buttons(self):
        self.add_button = ttk.Button(
            self.root,
            text="Добавить человека",
            command=self.open_add_window
        )
        self.add_button.pack(pady=10)

    def open_add_window(self):
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Добавление человека")
        self.add_window.geometry("400x450")
        self.create_form_fields()

    def create_form_fields(self):
        fields = [
            ("Имя", "first_name"),
            ("Фамилия", "last_name"),
            ("Отчество", "middle_name"),
            ("Дата рождения", "birth_date"),
            ("Дата смерти", "death_date"),
            ("Пол (m/f)", "gender")
        ]
        self.entries = {}
        for label_text, field_name in fields:
            label = ttk.Label(self.add_window, text=label_text)
            label.pack(pady=5)
            entry = ttk.Entry(self.add_window)
            entry.pack(pady=5)
            self.entries[field_name] = entry
        save_button = ttk.Button(
            self.add_window,
            text="Сохранить",
            command=self.save_person
        )
        save_button.pack(pady=10)

    def save_person(self):
        try:
            person = Person(
                first_name=self.entries["first_name"].get(),
                last_name=self.entries["last_name"].get(),
                middle_name=self.entries["middle_name"].get(),
                birth_date=self.entries["birth_date"].get(),
                death_date=self.entries["death_date"].get() or None,
                gender=self.entries["gender"].get()
            )
            self.database.add_person(person)
            self.add_window.destroy()
            self.refresh_table()
            messagebox.showinfo(
                "Успех",
                "Человек успешно добавлен!"
            )
        except ValueError as error:
            messagebox.showerror("Ошибка", str(error))

    def refresh_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.load_people()