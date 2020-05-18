season_month = dict(весна=[3, 4, 5], лето=[6, 7, 8], осень=[9, 10, 11], зима=[12, 1, 2])

month_num = int(input("Введите номер месяца от 1 до 12 - "))
for season, month in season_month.items():
    if month_num in month:
        print(season)



