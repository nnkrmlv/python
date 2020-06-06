def add_strings(arr_of_strings, file):
    # принимает на вход массив строк и файл. Записывает число с новой строки отдельно
    for el in arr_of_strings:
        new_str_el = el + "\n"
        file.write(new_str_el)


def sum_of_num(numbers):
    # принимает на вход массив строк, которые должны содержать числа, возвращает сумму чисел
    sum = 0
    for el in numbers:
        sum += int(el)
    return sum


with open("sum_of_num.txt", mode='w', encoding="utf-8") as sum_f:
    n = input("Введите набор чисел, разделенных пробелами: ")
    arr_of_numbers = n.split()
    try:
        total_sum = sum_of_num(arr_of_numbers)
        add_strings(arr_of_numbers, sum_f)
        print(total_sum)
    except ValueError:
        print("Некорректный ввод")
