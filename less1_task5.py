income = int(input("Введите сумму выручки - "))
expense = int(input("Введите сумму издержек - "))

profit = income - expense > 0
loss = expense - income > 0

rent = int((income - expense) / income * 100)

if profit:
    print("Фирма работает на прибыль. ")
    print("Процент рентабильности:", rent)
    worker = int(input("Сколько сотрудников в фирме? "))
    worker_inc = (income - expense) / worker
    print(f"Прибыль фирмы в расчете на одного сотрудника: {worker_inc:.2f}")
elif loss:
    print("Фирма работает в убыток. ")



