play = "д"
record = 7


while play == "д":
 import random
 secret = random.randint(1, 10)
 print("Я загадал число от 1 до 10, попробуй его угадать: ")
 answer = 0
 tries = 0
 max_tries = 7
 while answer != secret and tries < max_tries:
    answer = int(input("Твой вариант: "))
    tries += 1

    if answer > secret:
     print("Нет, меньше, твой вариант", answer)
    elif answer < secret:
     print("Нет, больше, твой вариант", answer)
    elif answer == secret:
     print("Правильно. Ты угадал за ", tries, "попытки")
 if tries < record:
       print("New record", tries)
       record = tries



 play = input("Хочешь продолжить? Д или Н: ").lower()



