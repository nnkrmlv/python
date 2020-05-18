string = input("Введите строку из нескольких слов, разделенных пробелами - ")
arr = list(string.split())

j = 0
for i in arr:
    print(j, ": ", i[:10],  end="\n")
    j += 1
