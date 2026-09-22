while True:
    num_first = float(input("Введите первое число: "))
    operator = input("Введите операцию (+, -, *, /, history): ")
    num_second = float(input("Введите второе число: "))

    if operator == "+":
      result = num_first+ num_second
      print(result)
      continue
    elif operator == "-":
      result = num_first - num_second
      print(result)
      continue
    elif operator == "*":
      result = num_first * num_second
      print(result)
      continue
    elif operator == "/":
      result = num_first / num_second
      print(result)
      continue
    else:
      print("Неизвестная операция")
      continue