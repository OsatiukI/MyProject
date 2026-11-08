products = []
def enter():
    while True:
        name = input("Введите название продукта (или 'стоп'): ")
        if name == "стоп":
            break
        while True:
            try:
                price = float(input("Введите цену продукта: ").replace(",", "."))
                break
            except ValueError:
                print("Только цифры!")
        product = {
            "name": name,
            "price": price
        }
        products.append(product)

def show_products():
    for product in products:
        print(product["name"], "-", product["price"], "гривен" )

def sum_products(products):
    total = 0
    for product in products:
        total += product["price"]
    return total

while True:
    print("1. Добавить расход")
    print("2. Список продутов")
    print("3. Сумма всех покупок")
    answer = int(input("Выбери действие: "))
    if answer == 1:
        enter()
    elif answer == 2:
        show_products()
    elif answer == 3:
        total = sum_products(products)
        print("Общая сумма:", total)

