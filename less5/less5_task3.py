with open("text_3.txt", "r", encoding="utf-8") as names_f:
    all_list = names_f.readlines()


    def salary_high():
        for string in all_list:
            words_in_string = string.split()
            if float(words_in_string[1]) > 20000:
                print(f"{words_in_string[0]}")


    def avr_salary():
        s,i = 0, 0
        for string in all_list:
            words_in_string = string.split()
            s += float(words_in_string[1])
            i += 1
        avr = s / i
        return avr

avr = avr_salary().__round__(2)
print("Зарплаты сотрудников свыше 20 000р: ")
salary_high()
print(f"Средняя зарплата среди сотрудников составляет {avr} рублей.")
