import json
import codecs

with open("text_7.txt", "r", encoding="utf-8") as companies:
    comp_income_lines = companies.readlines()  # читаем все строки в переменную, тип список строк
    total_income = 0  # сумма всех доходов
    i = 0  # переменная-счетчик. Количество элементов, которые учитываю в total_income
    my_dict1 = {}  # Словарь. Ключи - названия компаний, значения - доход
    for line in comp_income_lines:  # цикл для перебора строк в файле text_7.txt
        string_to_array = line.split()  # разбиваем на список, где 0эл -  название, (2 - 3)эл - доход

        company = string_to_array[0]
        income = int(string_to_array[2]) - int(string_to_array[3])
        pair = {company: income}

        my_dict1.update(pair)

        if income > 0:
            total_income += income
            i += 1
    avg_income = total_income / i
    my_dict2 = {"average_profit": avg_income}
    print(my_dict1)
    print(my_dict2)

    list_of_dicts = [my_dict1, my_dict2]
    print(list_of_dicts)

    with open("text_7_new.json", "w", encoding="utf-8") as write_f:
        json.dump(list_of_dicts, write_f, ensure_ascii=False, indent=2)
