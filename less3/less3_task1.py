def fun(x, y):
    try:
        z = x / y
    except ZeroDivisionError:
        print("На ноль делить нельзя. Введите число Y отличное от нуля.")
        return
    z = x / y
    return z


i = 1
while i < 3:
    x = float(input("Введите число X - "))
    y = float(input("Введите число Y - "))
    print(fun(x, y))
    i += 1



