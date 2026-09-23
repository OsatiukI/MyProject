numbers = list(map(int, input("Введите числа: ").split()))
print(numbers)
if not numbers:
    print("none")
elif len(numbers) == 1:
    print(numbers)
else:
  print(numbers[-1])
  mix = [numbers[-1]] + numbers[:-1]
  print(mix)