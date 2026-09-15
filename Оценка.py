print("Как зовут ученика: ")
name = input()
print("Введите пять оценок ученика", name)
a = int(input("Первая оценка: "))
b = int(input("Вторая оценка: "))
c = int(input("Тертья оценка: "))
d = int(input("Четвертая оценка: "))
e = int(input("Пятая оценка: "))
print("Результаты ученика :", name)

midresult = (a + b + c + d + e) / 5
print("Средний результат:", midresult)
maresult = max(a, b, c, d, e)
miresult = min(a, b, c, d, e)
print("Самая высокая оценка: ", maresult)
print("Самая низкая оценка: ", miresult)
if midresult > 3:
    print("Итоговая оценка : Хорошая")
else:
    print("Итоговая оценка : Плохая")