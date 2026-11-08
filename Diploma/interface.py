import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from person import Person
from datetime import date

class Application:

    def __init__(self, database):
        self.database = database
        self.root = tk.Tk()
        self.root.title("Управление данными о людях")
        self.root.geometry("1100x650")
        self.root.minsize(850, 500)
        # Цветовая палитра приложения
        self.colors = {
            "background": "#F4F6FA",
            "surface": "#FFFFFF",
            "primary": "#2563EB",
            "text": "#1E293B",
            "secondary": "#64748B",
            "border": "#E2E8F0"
        }
        # Настройка главного окна
        self.root.configure(
            bg=self.colors["background"]
        )
        # Настройка стилей элементов Tkinter
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(
            ".",
            font=("Arial", 10)
        )
        self.create_buttons()
        self.create_status_bar()
        self.create_table()
        self.load_people()
        self.root.mainloop()

    def create_table(self):
        columns = (
            "id",
            "first_name",
            "last_name",
            "middle_name",
            "birth_date",
            "death_date",
            "gender",
            "age"
        )
        # Настройка внешнего вида таблицы
        self.style.configure(
            "Treeview",
            background=self.colors["surface"],
            foreground=self.colors["text"],
            rowheight=35,
            font=("Arial", 10),
            fieldbackground=self.colors["surface"],
            borderwidth=0
        )
        # Настройка заголовков таблицы
        self.style.configure(
            "Treeview.Heading",
            background="#EAF0F8",
            foreground=self.colors["text"],
            font=("Arial", 10, "bold"),
            padding=(8, 12),
            relief="flat"
        )
        # Цвет выбранной строки
        self.style.map(
            "Treeview",
            background=[
                ("selected", "#DBEAFE")
            ],
            foreground=[
                ("selected", "#1E293B")
            ]
        )
        table_frame = ttk.Frame(
            self.root,
            padding=(15, 5, 15, 15)
        )
        table_frame.pack(
            fill="both",
            expand=True
        )
        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )
        # Заголовки столбцов
        self.tree.heading("id", text="ID")
        self.tree.heading("first_name", text="Имя")
        self.tree.heading("last_name", text="Фамилия")
        self.tree.heading("middle_name", text="Отчество")
        self.tree.heading("birth_date", text="Дата рождения")
        self.tree.heading("death_date", text="Дата смерти")
        self.tree.heading("gender", text="Пол")
        self.tree.heading("age", text="Возраст")
        # Ширина и выравнивание столбцов
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("first_name", width=130)
        self.tree.column("last_name", width=140)
        self.tree.column("middle_name", width=140)
        self.tree.column("birth_date", width=120, anchor="center")
        self.tree.column("death_date", width=120, anchor="center")
        self.tree.column("gender", width=100, anchor="center")
        self.tree.column("age", width=90, anchor="center")
        # Двойной щелчок открывает подробную информацию
        self.tree.bind(
            "<Double-1>",
            self.show_person_details
        )
        # Вертикальная прокрутка
        scrollbar_y = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )
        # Горизонтальная прокрутка
        scrollbar_x = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.tree.xview
        )
        self.tree.configure(
            yscrollcommand=scrollbar_y.set,
            xscrollcommand=scrollbar_x.set
        )
        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew"
        )
        scrollbar_y.grid(
            row=0,
            column=1,
            sticky="ns"
        )
        scrollbar_x.grid(
            row=1,
            column=0,
            sticky="ew"
        )
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

    def load_people(self):
        # Очищаем таблицу перед загрузкой записей
        self.tree.delete(*self.tree.get_children())
        # Настраиваем чередование цветов строк
        self.tree.tag_configure(
            "evenrow",
            background="#FFFFFF"
        )
        self.tree.tag_configure(
            "oddrow",
            background="#F1F5F9"
        )
        # Получаем все записи из базы данных
        persons = self.database.get_all_persons()
        for person in persons:
            # Создаём объект человека
            person_object = Person(
                first_name=person[1],
                last_name=person[2],
                middle_name=person[3],
                birth_date=date.fromisoformat(person[4]),
                death_date=date.fromisoformat(person[5]) if person[5] else None,
                gender=person[6]
            )
            # Рассчитываем возраст
            age = person_object.calculate_age()
            # Преобразуем обозначение пола в текст
            if person[6] == "m":
                gender_text = "Мужской"
            elif person[6] == "f":
                gender_text = "Женский"
            else:
                gender_text = "Не указан"
            # Подготавливаем данные для отображения
            values = (
                person[0],
                person[1],
                person[2] or "—",
                person[3] or "—",
                person[4],
                person[5] or "—",
                gender_text,
                age
            )
            # Определяем цвет текущей строки
            row_tag = (
                "evenrow"
                if len(self.tree.get_children()) % 2 == 0
                else "oddrow"
            )
            # Добавляем запись в таблицу
            self.tree.insert(
                "",
                "end",
                values=values,
                tags=(row_tag,)
            )
        # Обновляем количество записей
        self.update_status()

    def create_buttons(self):
        toolbar = ttk.Frame(
            self.root,
            padding=(15, 12)
        )
        toolbar.pack(fill="x")
        # Настройка панели
        self.style.configure(
            "Toolbar.TFrame",
            background=self.colors["surface"]
        )
        toolbar.configure(style="Toolbar.TFrame")
        # Кнопка добавления
        self.add_button = ttk.Button(
            toolbar,
            text="+ Добавить",
            command=self.open_add_window,
            style="Primary.TButton"
        )
        self.add_button.pack(side="left", padx=5)
        # Кнопка редактирования
        self.edit_button = ttk.Button(
            toolbar,
            text="Редактировать",
            command=self.open_edit_window,
            style="Toolbar.TButton"
        )
        self.edit_button.pack(side="left", padx=5)
        # Кнопка удаления
        self.delete_button = ttk.Button(
            toolbar,
            text="Удалить",
            command=self.delete_person,
            style="Toolbar.TButton"
        )
        self.delete_button.pack(side="left", padx=5)
        # Кнопка отображения всех записей
        self.show_all_button = ttk.Button(
            toolbar,
            text="Показать всех",
            command=self.refresh_table,
            style="Toolbar.TButton"
        )
        self.show_all_button.pack(side="left", padx=5)
        # Поле поиска
        self.search_entry = ttk.Entry(
            toolbar,
            width=30,
            font=("Arial", 10)
        )
        self.search_entry.pack(side="right", padx=5, ipady=5)
        # Кнопка поиска
        self.search_button = ttk.Button(
            toolbar,
            text="Найти",
            command=self.search_people,
            style="Primary.TButton"
        )
        self.search_button.pack(side="right", padx=5)
        # Поиск по нажатию Enter
        self.search_entry.bind(
            "<Return>",
            lambda event: self.search_people()
        )
        # Стили кнопок
        self.style.configure(
            "Primary.TButton",
            background=self.colors["primary"],
            foreground="#FFFFFF",
            font=("Arial", 10, "bold"),
            padding=(14, 8),
            borderwidth=0
        )
        self.style.map(
            "Primary.TButton",
            background=[
                ("active", "#1D4ED8"),
                ("pressed", "#1E40AF")
            ]
        )
        self.style.configure(
            "Toolbar.TButton",
            background="#FFFFFF",
            foreground=self.colors["text"],
            font=("Arial", 10),
            padding=(14, 8),
            borderwidth=1,
            relief="solid"
        )
        self.style.map(
            "Toolbar.TButton",
            background=[
                ("active", "#EFF6FF"),
                ("pressed", "#DBEAFE")
            ]
        )

    def create_status_bar(self):
        self.status_frame = ttk.Frame(
            self.root,
            padding=(20, 12)
        )
        self.status_frame.pack(
            side="bottom",
            fill="x"
        )
        self.style.configure(
            "Status.TFrame",
            background=self.colors["surface"]
        )
        self.status_frame.configure(
            style="Status.TFrame"
        )
        self.status_label = ttk.Label(
            self.status_frame,
            text="Записей в таблице: 0",
            font=("Arial", 10, "bold"),
            foreground=self.colors["primary"],
            background=self.colors["surface"]
        )
        self.status_label.pack(side="left")

    def update_status(self):
        count = len(self.tree.get_children())

        self.status_label.config(
            text=f"Записей в таблице: {count}"
        )

    def open_add_window(self):
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Добавление человека")
        self.add_window.geometry("450x500")
        self.add_window.minsize(450, 500)
        self.add_window.configure(
            bg=self.colors["background"]
        )
        self.add_window.transient(self.root)
        self.add_window.grab_set()
        self.create_form_fields()
        self.save_button.config(
            command=self.save_person,
            text="Сохранить"
        )

    def create_form_fields(self):
        fields = [
            ("Имя", "first_name"),
            ("Фамилия", "last_name"),
            ("Отчество", "middle_name"),
            ("Дата рождения", "birth_date"),
            ("Дата смерти", "death_date"),
            ("Пол (m/f)", "gender")
        ]
        # Белый фон для области формы
        form_frame = ttk.Frame(
            self.add_window,
            padding=20,
            style="Form.TFrame"
        )
        form_frame.pack(fill="both", expand=True)
        self.style.configure(
            "Form.TFrame",
            background="#FFFFFF"
        )
        self.style.configure(
            "Form.TLabel",
            background="#FFFFFF",
            foreground=self.colors["text"],
            font=("Arial", 10)
        )
        self.entries = {}
        for label_text, field_name in fields:
            label = ttk.Label(
                form_frame,
                text=label_text,
                style="Form.TLabel"
            )
            label.pack(anchor="w", pady=(5, 2))
            entry = ttk.Entry(
                form_frame,
                font=("Arial", 10)
            )
            entry.pack(fill="x", pady=(0, 8), ipady=4)
            self.entries[field_name] = entry
        self.save_button = ttk.Button(
            form_frame,
            text="Сохранить",
            command=self.save_person,
            style="Primary.TButton"
        )
        self.save_button.pack(pady=15)

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


    def delete_person(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning(
                "Предупреждение",
                "Сначала выберите человека в таблице!"
            )
            return
        person_data = self.tree.item(selected_item[0], "values")
        person_id = person_data[0]
        confirm = messagebox.askyesno(
            "Подтверждение",
            "Вы действительно хотите удалить этого человека?"
        )
        if confirm:
            self.database.delete_person(person_id)
            self.refresh_table()
            messagebox.showinfo(
                "Успех",
                "Человек успешно удалён!"
            )

    def search_people(self):
        search_text = self.search_entry.get().strip()
        if not search_text:
            self.refresh_table()
            return
        for item in self.tree.get_children():
            self.tree.delete(item)
        persons = self.database.search_person(search_text)
        for person in persons:
            person_object = Person(
                first_name=person[1],
                last_name=person[2],
                middle_name=person[3],
                birth_date=date.fromisoformat(person[4]),
                death_date=date.fromisoformat(person[5]) if person[5] else None,
                gender=person[6]
            )
            age = person_object.calculate_age()
            self.tree.insert(
                "",
                "end",
                values=person + (age,)
            )
        self.update_status()

    def open_edit_window(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning(
                "Предупреждение",
                "Сначала выберите человека в таблице!"
            )
            return
        # Получаем данные выбранного человека
        person_data = self.tree.item(
            selected_item[0],
            "values"
        )
        self.edit_person_id = person_data[0]
        # Создаём окно редактирования
        self.add_window = tk.Toplevel(self.root)
        self.add_window.title("Редактирование человека")
        self.add_window.geometry("450x500")
        self.add_window.minsize(450, 500)
        self.add_window.configure(
            bg=self.colors["background"]
        )
        self.add_window.transient(self.root)
        self.add_window.grab_set()
        # Создаём поля формы
        self.create_form_fields()
        # Настраиваем кнопку сохранения
        self.save_button.config(
            command=self.update_person,
            text="Сохранить изменения"
        )
        # Названия полей
        field_names = [
            "first_name",
            "last_name",
            "middle_name",
            "birth_date",
            "death_date",
            "gender"
        ]
        # Заполняем поля существующими данными
        for index, field_name in enumerate(field_names):
            value = person_data[index + 1]
            if field_name in ("birth_date", "death_date") and value:
                from datetime import date
                value = date.fromisoformat(value).strftime("%d.%m.%Y")
            self.entries[field_name].insert(0, value)

    def update_person(self):
        try:
            person = Person(
                first_name=self.entries["first_name"].get(),
                last_name=self.entries["last_name"].get(),
                middle_name=self.entries["middle_name"].get(),
                birth_date=self.entries["birth_date"].get(),
                death_date=self.entries["death_date"].get() or None,
                gender=self.entries["gender"].get()
            )
            self.database.update_person(
                self.edit_person_id,
                person
            )
            self.add_window.destroy()
            self.refresh_table()
            messagebox.showinfo(
                "Успех",
                "Данные человека успешно обновлены!"
            )
        except ValueError as error:
            messagebox.showerror("Ошибка", str(error))

    def show_person_details(self, event):
        selected_item = self.tree.selection()
        if not selected_item:
            return
        person_data = self.tree.item(
            selected_item[0],
            "values"
        )
        details_window = tk.Toplevel(self.root)
        details_window.title("Информация о человеке")
        details_window.geometry("450x430")
        details_window.resizable(False, False)
        details_window.configure(
            bg="#FFFFFF"
        )
        details_window.transient(self.root)
        # Основная область окна
        details_frame = ttk.Frame(
            details_window,
            padding=25,
            style="Details.TFrame"
        )
        details_frame.pack(fill="both", expand=True)
        # Стили окна
        self.style.configure(
            "Details.TFrame",
            background="#FFFFFF"
        )
        self.style.configure(
            "Details.Title.TLabel",
            background="#FFFFFF",
            foreground=self.colors["primary"],
            font=("Arial", 16, "bold")
        )
        self.style.configure(
            "Details.Label.TLabel",
            background="#FFFFFF",
            foreground=self.colors["secondary"],
            font=("Arial", 10)
        )
        self.style.configure(
            "Details.Value.TLabel",
            background="#FFFFFF",
            foreground=self.colors["text"],
            font=("Arial", 10, "bold")
        )
        # Заголовок
        title_label = ttk.Label(
            details_frame,
            text=f"{person_data[1]} {person_data[2]}",
            style="Details.Title.TLabel"
        )
        title_label.pack(anchor="w", pady=(0, 20))
        # Информация о человеке
        fields = [
            ("ID", person_data[0]),
            ("Имя", person_data[1]),
            ("Фамилия", person_data[2]),
            ("Отчество", person_data[3]),
            ("Дата рождения", person_data[4]),
            ("Дата смерти", person_data[5] or "Не указана"),
            ("Пол", person_data[6] or "Не указан"),
            ("Возраст", f"{person_data[7]} лет")
        ]
        for label_text, value in fields:
            row_frame = ttk.Frame(
                details_frame,
                style="Details.TFrame"
            )
            row_frame.pack(fill="x", pady=6)
            ttk.Label(
                row_frame,
                text=f"{label_text}:",
                style="Details.Label.TLabel",
                width=18
            ).pack(side="left")
            ttk.Label(
                row_frame,
                text=value,
                style="Details.Value.TLabel"
            ).pack(side="left")
        # Кнопка закрытия
        close_button = ttk.Button(
            details_frame,
            text="Закрыть",
            command=details_window.destroy,
            style="Primary.TButton"
        )
        close_button.pack(anchor="e", pady=(20, 0))