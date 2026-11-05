from student import Student
from group import Group

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)

print(gr)

assert gr.find_student('Jobs') == st1
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')

print(gr)

import os
import zipfile

folder = os.path.dirname(os.path.abspath(__file__))

with zipfile.ZipFile(os.path.join(folder, "ДЗ 15.2.zip"), "w", zipfile.ZIP_DEFLATED) as zipf:
    zipf.write(os.path.join(folder, "student.py"), "student.py")
    zipf.write(os.path.join(folder, "group.py"), "group.py")
    zipf.write(os.path.join(folder, "main.py"), "main.py")

print("Архив сохранён!")
