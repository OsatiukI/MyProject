from exceptions import GroupLimitError


class Group:
    max_students = 10


    def __init__(self, number):
        self.number = number
        self.group = set()


    def __str__(self):
        students = "\n".join(str(student) for student in self.group)
        return f"Number: {self.number}\n{students}"


    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise GroupLimitError(
                "A group cannot contain more than 10 students."
            )
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