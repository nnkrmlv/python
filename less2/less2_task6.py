goods = []
i, j = 1, 0

while i < 3:
    good_val = input("Введите название товара - ")
    price_val = input("Введите цену товара - ")
    amount_val = input("Введите количество товара - ")
    measure_val = input("Введите единицу измерения товара товара - ")



    while i >= 1:
        d = dict(good="", price="", amount="", measure="")
        d.update({"good": good_val, "price": price_val, "amount": amount_val, "measure": measure_val})
        tup = (i, d)
        goods.insert(i, tup)
        print(goods)
        i += 1
        break


