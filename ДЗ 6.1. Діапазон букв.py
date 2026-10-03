import string
answer = input("Введите две буквы: ")
lettrs = answer.split("-")
start = string.ascii_letters.find(lettrs[0])
finish = string.ascii_letters.find(lettrs[1])
print(string.ascii_letters[start:finish+1])
