class GroupLimitError(Exception):
    """Исключение при превышении количества студентов в группе."""
    pass


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name


    def __str__(self):
        return f"{self.gender}, {self.age} years, {self.first_name} {self.last_name}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book


    def __str__(self):
        return f"{super().__str__()}, record book: {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()


    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + '\n'
        return f'Number: {self.number}\n{all_students}'



    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupLimitError("В группе не может быть больше 10 студентов")
        self.group.add(student)


    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None


    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student is not None:
            self.group.remove(student)


gr = Group("group bb")
try:
    for i in range(11):
        student = Student(
            'Male', 20, f'Student{i}', f'LastName{i}', f'AN{i}'
        )
        gr.add_student(student)
except GroupLimitError as error:
    print(error)

print(gr)