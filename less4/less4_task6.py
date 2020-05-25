from itertools import count, cycle


def generate_int():
    array = []
    n = int(input("Введите число, с которого будет генерироваться массив - "))
    for el in count(n):
        if el > n * 10:
            break
        else:
            array.append(el)
    return array


def repeat_el(array, i=0):
    for el in cycle(array):
        if i > 100:
            break
        print(el)
        i += 1


print(repeat_el(generate_int()))
