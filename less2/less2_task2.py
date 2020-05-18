num_elem = int(input("Какое количество элементов будет в списке? "))

i = 0
the_list = []
while i < num_elem:
    the_list.append(input(f"Введите элемент № {i+1} - "))
    i += 1
print(the_list)

new_list = []
j = 0
while len(new_list) != len(the_list) - 1:
    if j % 2 == 0:
        j += 1
        new_list.append(the_list[j])
        j -= 1
    else:
        j -= 1
        new_list.append(the_list[j])
        j += 1
    j = j + 1

if num_elem % 2 != 0:
    new_list.append(the_list[j])
else:
    new_list.append(the_list[j - 1])

print("Новый список элементов, где соседние элементы поменялись местами - ", new_list)



