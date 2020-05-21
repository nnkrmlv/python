n = input("What is your name? ")
s = input("What is your surname? ")
t = input("What is your town? ")
d = input("Print the date of birth - ")
e = input("Print you email address - ")
p = input("Print your telephone number - ")


def function(name, surname, date, town, email, phone_number):
    note = str(f"{name}, {surname}, {date}, {town}, {email}, {phone_number}")
    return note


print(f"Информация о пользователе: {function(name=n, surname=s, date=d, town=t, email=e, phone_number=p)}")



