# Контрольная

#Задание 1

# myName = input("Введите ваше имя: ")
# mySurname = input("Введите вашу фамилию: ")
# myAge = input("Введите ваш возраст: ")
# myByear = input("Введите ваш год рождения: ")
# print(f"Карточка пользователя:\nИмя:  {myName}\nФамилия:  {mySurname}\nВозраст:  {myAge}\nГод рождения:  {myByear}")

#Задание 2

# vybor = int(input("Выберите загадку(1, 2 или 3): "))
# if vybor == 1:
#     print("Кто его раздевает, тот слезы проливает. Что это?")
#     otvet = input("Введите ответ: ")
#     if otvet == "Лук":
#         print("Верно!")
#     else:
#         print("Не верно!")
# elif vybor == 2:
#     print("Зимой и летом одним цветом. Что это?")
#     otvet = input("Введите ответ: ")
#     if otvet == "Елка":
#         print("Верно!")
#     else:
#         print("Не верно!")
# elif vybor == 3:
#     print("Два конца, два кольца, посередине гвоздик. Что это?")
#     otvet = input("Введите ответ: ")
#     if otvet == "Ножницы":
#         print("Верно!")
#     else:
#         print("Не верно!")
# else:
#     print("Ошибка выбора!")

#Задание 3

# import random
# uch = random.randint(0,10)
# popytka = 1
# vybnum = int(input("Введите число от 0 до 10\n>"))
# popytka += 1
# while vybnum != uch:
#     vybnum = int(input("Повторите попытку\n>"))
#     if uch < vybnum:
#         print("Ваше число больше!")
#         popytka += 1
#     elif uch > vybnum:
#         print("Ваше число меньше!")
#         popytka += 1
#     else:
#         print(f"Вы угадали, это число {uch}!\nВы использовали {popytka} попыток ")
#         popytka += 1
#         break

#Задание 4 

weekList = [
    {
        "weekday" : "Понедельник",
        "lesson1" : "Математика",
        "lesson2" : "Физика",
        "lesson3" : "Информатика",
        "lesson4" : "Физкультура",
        "vyhodnoy" : "",

    },
    {
        "weekday" : "Вторник",
        "lesson1" : "Математика",
        "lesson2" : "Физика",
        "lesson3" : "Информатика",
        "lesson4" : "",
        "vyhodnoy" : "",
    },
    {
        "weekday" : "Среда",
        "lesson1" : "Литература",
        "lesson2" : "Физика",
        "lesson3" : "Информатика",
        "lesson4" : "Математика",
        "vyhodnoy" : "",
    },
    {
        "weekday" : "Четверг",
        "lesson1" : "Литература",
        "lesson2" : "Физика",
        "lesson3" : "Информатика",
        "lesson4" : "Черчение",
        "vyhodnoy" : "",
    },
    {
        "weekday" : "Пятница",
        "lesson1" : "Литература",
        "lesson2" : "Физика",
        "lesson3" : "Ин. язык",
        "lesson4" : "Математика",
        "vyhodnoy" : "",
    },
    {
        "weekday" : "Суббота",
        "lesson1" : "",
        "lesson2" : "",
        "lesson3" : "",
        "lesson4" : "",
        "vyhodnoy" : "Выходной",
    },
    {
        "weekday" : "Воскресение",
        "lesson1" : "",
        "lesson2" : "",
        "lesson3" : "",
        "lesson4" : "",
        "vyhodnoy" : "Выходной",
    },    
]
for i in range(0,len(weekList)):
    print(f"День недели - {weekList[i]['weekday']}")
    print(f"1 - {weekList[i]['lesson1']}")
    print(f"2 - {weekList[i]['lesson2']}")
    print(f"3 - {weekList[i]['lesson3']}")
    print(f"4 - {weekList[i]['lesson4']}")
    print(f"{weekList[i]['vyhodnoy']}")