import random
numbers = []
acc = random.randint(3, 10)
for i in range(acc):
    numbers.append(random.randint(1, 10))
#print(numbers)
result = []
result.append(numbers[0])
result.append(numbers[2])
result.append(numbers[-2])
print(numbers)
print(result)