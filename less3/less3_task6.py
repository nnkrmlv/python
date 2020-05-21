words = input("Введите слова из маленьких латинских букв, разделенные пробелами ")
words = words.lower()
array = words.split()  # массив из строк нижнего регистра только


def inc_func(string):  # функция приводит строку к виду Bbbb
    return string.title()


def is_latin(c):  # На вход принимает символ, возвращает true или false
    return 'a' <= c <= 'z'  # Вернет true если c - лат. буква


def check(string):  # функция принимает на вход строку, возвращает результат проверки на латинские буквы
    for c in string:
        if not is_latin(c):
            print("Некорректный ввод")
            return False
        else:
            return True


for el in array:
    if check(el) is True:  # Если элемент прошел проверку на лат. буквы, то вызываем функцию inc_func(), иначе выводим сообщение "Некорректный ввод" и делаем break
        print(inc_func(el))
    else:
        break

