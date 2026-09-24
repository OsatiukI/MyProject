while True:
    num_first = float(input("Введите первое число: "))
    operator = input("Введите операцию (+, -, *, /): ")
    num_second = float(input("Введите второе число: "))

    if operator == "+":
      result = num_first+ num_second
    elif operator == "-":
      result = num_first - num_second
    elif operator == "*":
      result = num_first * num_second
    elif operator == "/":
        if num_second == 0:
            print("На ноль делить нельзя!")
            continue
        result = num_first / num_second
    else:
        print("Неизвестная операция")
        continue
    print(result)