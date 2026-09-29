import string
import keyword
result = True

answer = input("Введите строку: ")
if answer[0].isdigit():
    result = False
for item in answer:
    if item.isupper():
        result = False
    if item == " ":
        result = False
    if item in string.punctuation and item !="_":
        result = False
if "__" in answer:
    result = False
if answer in keyword.kwlist:
    result = False

print(result)