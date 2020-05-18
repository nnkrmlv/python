rate = [7, 5, 3, 3, 2]
# rate = [7, 5, 3, 3, 3, 2]
# rate = [99, 7, 5, 3, 3, 3, 2]
# rate = [99, 7, 5, 3, 3, 3, 2, 0]



while True:
    new_el = int(input("Добавьте элемент в структуру \"Рейтинг\" - "))  # новый элемент это 0
    if new_el <= min(set(rate)):
        rate.append(new_el)
    else:
        i = 0  # индекс, на который мы собираемся вставить элемент new_elem
        for el in rate:     # el <- 7, 5, 3, ...
            # отсюда
            if new_el >= el:
                break  # на какую строчку я попаду?
            i += 1
            # до сюда
        # сюда попадаем после break
        rate.insert(i, new_el)












