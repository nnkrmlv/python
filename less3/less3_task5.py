i = 0
s = 0
stop = False


def ask_array():
    n = input("Введите числа, разделенные пробелами. Для выхода из программы нажмите \"Q\". ")
    array = n.split()  # "rr uuu iii" --> ["rr", "uuu", "iii"]
    return array


while not stop:
    arr = ask_array()

    for el in arr:
        if el.lower() == "q":
            print("Вы вышли из программы.")
            stop = True
        else:
            s = s + int(el)
            i += 1
    print(f"Итоговая сумма: {s}")
