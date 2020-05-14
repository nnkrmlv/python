number = int(input("Введите число - "))
max = 0

new_number = abs(number)
while new_number != 0:
    n = new_number % 10
    if max < n:
        max = n
    new_number = new_number // 10


print(f"Максимальная цифра в числе {number} - {max}")
