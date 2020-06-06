grocery_file = open("grocery_file.txt", "r", encoding="utf-8")


def counter():
    all_lines = grocery_file.readlines()
    i = 0
    for string in all_lines:
        i += 1
        print(f"Line №{i}: has {len([string])} word - {string}")
    print(f"Total lines: {i}")


counter()
grocery_file.close()
