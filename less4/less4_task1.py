from sys import argv

try:
    name, hours, money_per_hour, bonus = argv

    print(f"Количество отработанных часов: {hours}")
    print(f"Количество денег, заработанных за час работы: {money_per_hour}")
    print(f"Премия: {bonus}")
    total = (int(hours) * int(money_per_hour)) + int(bonus)
    print(f"Заработная плата сотрудника - {total}р.")

except ValueError:
    print("Неверное количество параметров")
