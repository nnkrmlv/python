n = int(input("Введите число - "))
j = 1


def fact(n):
    current_el = 1
    for i in tuple(range(1, n + 1)):
        current_el = current_el * i
        yield current_el


g = fact(n)  # Возвращает итератор

# для каждого элемента el из итератора g
for el in g:  # el принимает значения факториала = [1], 2, 6, 24, 120, 720, ...
    print(f"{j}! = {el}")
    j += 1
