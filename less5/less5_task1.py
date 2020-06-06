grocery_list = []
stop = False
i = 0
print("Hello! Glad to see you! Create the grocery list please. Print \"stop\" to cancel.\n")

while stop is False:
    grocery_file = open("grocery_file.txt", "a", encoding="utf-8")
    n = input(f"№{i + 1}:  ")
    if "stop" in n:
        stop = True
        grocery_file.close()
        break

    grocery_list.append(n)
    grocery_file.write(f"{i + 1}: {grocery_list[i]}\n")
    i += 1


