dictionary = dict(One="Один", Two="Два", Three="Три", Four="Четыре")

with open("text_4.txt", "r", encoding="utf-8") as numbers:
    new_f = open("rus_counter.txt", "w", encoding="utf-8")

    lines = numbers.readlines()


def write_rus_str():
    for line in lines:
        eng_number = (line.split())[0]
        get_russian_c = dictionary.get(eng_number)
        new_line = line.replace(eng_number, get_russian_c)
        new_f.write(new_line)


write_rus_str()
new_f.close()
