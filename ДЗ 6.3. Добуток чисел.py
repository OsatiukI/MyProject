answer = int(input("Введите число: "))
while answer > 9:
    result = 1
    while answer > 0:
        digit = answer % 10
        result = result * digit
        answer = answer // 10
    answer = result
print(answer)

