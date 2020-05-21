x = int(input("Введите положительное число x: "))
y = int(input("Введите отрицательное число y: "))


def my_func(x, y):
    if x <= 0 or y > 0:
        print("Некорректный ввод данных.")

    p = (1 / (x ** abs(y)))
    return round(p, 4)


def my_func_2(x, y):
    """x возводим в степень y, y - отрицательное"""
    i = 1
    if x <= 0 or y > 0 :
        print("Некорректный ввод данных.")

    result = 1 / x
    while i < abs(y):
        result = result / x
        i += 1
    return round(result, 4)


print(my_func(x, y))
print(my_func_2(x, y))







