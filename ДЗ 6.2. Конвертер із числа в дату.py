while True:  #Сделал через цикл, что бы при вводе чимла больше, можно было еще раз запустить
    second = int(input("Ввкдите число: "))
    if not 0 <= second < 8640000:
        print("Введите число от 0 до 8639999")
        continue
    day = second // 86400
    day_after = second % 86400
    hour = day_after // 3600
    hour_after = day_after % 3600
    minute = hour_after // 60
    minute_after = hour_after % 60
    hour = str(hour).zfill(2)
    minute = str(minute).zfill(2)
    minute_after = str(minute_after).zfill(2)
    if day % 10 == 1 and day % 100 != 11:
        days = " день"
    elif day % 10 in (2, 3, 4,) and not (12 <= day % 100 <= 14):
        days = "дні"
    else:
        days = "днів"
    print(str(day) + " " + days + ", " + hour + ":" + minute + ":" + minute_after)