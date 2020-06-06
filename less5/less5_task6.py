with open("text_6.txt", "r", encoding="utf-8") as obj:
    lines = obj.readlines()
    schedule = {}


    for line in lines:
        arr_from_string = line.split()
        # print(arr_from_string)
        name = arr_from_string[0]
        # print(name)
        hours = arr_from_string[1:]
        # print(hours)
        s = 0
        sum = 0
        i = 0



        for el in hours:    # "-", "30(пр)", "8(лаб)"
            if el == "-":
                sum += 0
            else:
                d = ("")  # строка, которую нужно превратить в число
                digits_string = [c for c in el if c.isdigit()]
                d = d.join(digits_string)
                # print(d)
                number = int(d)
                sum += number
        dict_pair = {name: sum for el in name}
        print(dict_pair)












