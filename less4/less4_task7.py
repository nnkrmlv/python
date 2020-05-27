n = int(input("Введите число - "))
j = 0


def fact(n, current_el=1):
    for i in tuple(range(1, n + 1)):
        current_el = current_el * i
        yield current_el


g = fact(n)
try:
    for el in g:
        print("1! = 1")
        while True:
            print(f"{el + j + 1}! = {next(g)}")
            j += 1
except StopIteration:
    print("")
