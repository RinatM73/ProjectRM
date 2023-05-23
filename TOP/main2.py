# Задача 3

# x = int(input("Введите число месяца (от 1 до 12): "))
# if x == (1 or 2 or 12):
#     print("Zima")
# elif x == (3 or 4 or 5):
#     print("Vesna")
# elif x == (6 or 7 or 8):
#     print("Osen'")
# elif x == (9 or 10 or 11):
#     print("Zima")
# else:
#     print("Oshibka")

# Проверка високосного года

x = int(input("Введите год: "))
if x % 4 != 0:
    print("Год обычный")
elif x % 4 == 0:
    if x % 100 != 0:
        print("Год високосный")
    elif x % 100 == 0:
        if x % 400 == 0:
            print("Год високосный")
        else:
            print("Год обычный")
    else:
        print("ошибка")
else:
    print("ошибка")
