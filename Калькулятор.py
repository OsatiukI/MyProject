while True:
    try:
        num_first = float(input("Введите первое число: "))
    except ValueError:
        print("Ввелите число!")
        continue
    operator = input("Введите операцию (+, -, *, /): ")
    try:
        num_second = float(input("Введите второе число: "))
    except ValueError:
        print("Ввелите число!")
        continue

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
    answer = input("Продолжить? yes или y? ").lower()
    if answer != "yes" and answer != "y":
        break
