x = int(input("Введите ваш возраст: "))
if 0 <= x < 12:
    print("Вы ребенок")
elif 12 <= x < 18:
    print("Вы подросток")
elif 18 <= x < 60:
    print("Вы взрослый")
else:
    print("Вы пенсионер")