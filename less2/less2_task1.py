my_list = (1, "Hi", 1.4, "London", [1, 54, 89], {4, 7, 9, "light"}, True, 45, {'flat': 163, 'home': 2})

real_list = list(my_list)
print(real_list)

for i in real_list:
    print(type(i), i)

