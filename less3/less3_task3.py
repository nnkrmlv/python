x = int(input("Введите значение числа x: "))
y = int(input("Введите значение числа y: "))
z = int(input("Введите значение числа z: "))


def my_func(x, y, z):
    m = min(x, y, z)
    s = x + y + z - m
    return s


print(f"Сумма максимальных двух элементов равна: {my_func(x, y, z)}")
