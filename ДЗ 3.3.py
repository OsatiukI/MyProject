numbers = list(map(int, input("Введите числа: ").split()))
print(numbers)
if len(numbers) % 2:
    first_part = numbers[:len(numbers) // 2 + 1]
    second_part = numbers[len(numbers) // 2 + 1:]
    result = [first_part, second_part]
    print(result)
elif len(numbers) % 2 == 0:
    first_part = numbers[:len(numbers) // 2]
    second_part = numbers[len(numbers) // 2:]
    result = [first_part, second_part]
    print(result)