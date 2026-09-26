numbers = [5,0,6,7,0,8,99,90,0,0]
result = []
for number in numbers:
    if number != 0:
        result.append(number)
for number in numbers:
    if number == 0:
        result.append(number)
numbers = result
print(numbers)