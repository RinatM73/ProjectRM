# Задание 1

# myName = input("Введите ваше имя: ")
# mySurname = input("Введите вашу фамилию: ")
# myAge = input("Введите ваш возраст: ")
# myByear = input("Введите ваш год рождения: ")
# print(f"Карточка пользователя:\nИмя:  {myName}\nФамилия:  {mySurname}\nВозраст:  {myAge}\nГод рождения:  {myByear}")

# Задание 2

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

# Задание 3

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

# Задание 4 

# weekList = [
#     {
#         "weekday" : "Понедельник",
#         "lesson1" : "Математика",
#         "lesson2" : "Физика",
#         "lesson3" : "Информатика",
#         "lesson4" : "Физкультура",
#         "vyhodnoy" : "",

#     },
#     {
#         "weekday" : "Вторник",
#         "lesson1" : "Математика",
#         "lesson2" : "Физика",
#         "lesson3" : "Информатика",
#         "lesson4" : "",
#         "vyhodnoy" : "",
#     },
#     {
#         "weekday" : "Среда",
#         "lesson1" : "Литература",
#         "lesson2" : "Физика",
#         "lesson3" : "",
#         "lesson4" : "",
#         "vyhodnoy" : "",
#     },
#     {
#         "weekday" : "Четверг",
#         "lesson1" : "Литература",
#         "lesson2" : "Физика",
#         "lesson3" : "Информатика",
#         "lesson4" : "Черчение",
#         "vyhodnoy" : "",
#     },
#     {
#         "weekday" : "Пятница",
#         "lesson1" : "Литература",
#         "lesson2" : "Физика",
#         "lesson3" : "Ин. язык",
#         "lesson4" : "",
#         "vyhodnoy" : "",
#     },
#     {
#         "weekday" : "Суббота",
#         "lesson1" : "",
#         "lesson2" : "",
#         "lesson3" : "",
#         "lesson4" : "",
#         "vyhodnoy" : "Выходной",
#     },
#     {
#         "weekday" : "Воскресение",
#         "lesson1" : "",
#         "lesson2" : "",
#         "lesson3" : "",
#         "lesson4" : "",
#         "vyhodnoy" : "Выходной",
#     },    
# ]
# for i in range(0,len(weekList)):
#     if weekList[i]["weekday"] == "Понедельник" or weekList[i]["weekday"] == "Четверг":
#         print(f"День недели - {weekList[i]['weekday']}")
#         print(f"1 - {weekList[i]['lesson1']}  8.00 - 10.15")
#         print(f"2 - {weekList[i]['lesson2']}  10.20 - 11.25")
#         print(f"3 - {weekList[i]['lesson3']}  11.30 - 12.25")
#         print(f"4 - {weekList[i]['lesson4']}  13.00 - 14.00\n")
#     elif weekList[i]["weekday"] == "Вторник" or weekList[i]["weekday"] == "Пятница":
#         print(f"День недели - {weekList[i]['weekday']}")
#         print(f"1 - {weekList[i]['lesson1']}  8.00 - 10.15")
#         print(f"2 - {weekList[i]['lesson2']}  10.20 - 11.25")
#         print(f"3 - {weekList[i]['lesson3']}  11.30 - 12.25\n")
#     elif weekList[i]["weekday"] == "Среда":
#         print(f"День недели - {weekList[i]['weekday']}")
#         print(f"1 - {weekList[i]['lesson1']}  8.00 - 10.15")
#         print(f"2 - {weekList[i]['lesson2']}  10.20 - 11.25\n")
#     else:
#         print(f"День недели - {weekList[i]['weekday']}")
#         print(f"{weekList[i]['vyhodnoy']}\n")

#Задание 5

regList = []
while True:
    vybor = int(input("Выберите действие\n1 - Регистрация\n2 - Вход\n"))
    if vybor == 1:
        print("Регистрация")
        while True:
            inforeg = {
            "namePerson" : "",
            "surnamePerson" : "",
            "loginPerson" : "",
            "passwordPerson" : "",
            }
            while True:
                myLogin = input("Введите логин: ")
                if len(regList) > 0:
                    for i in range(0,len(regList)):
                        if myLogin != regList[i]["loginPerson"]:
                            inforeg["loginPerson"] = myLogin
                        elif len(regList) - 1 == i:
                            print("Логин занят, введите другой!")
                            inforeg["loginPerson"] = ""
                            break
                else:
                    inforeg["loginPerson"] = myLogin
                if len(inforeg["loginPerson"]) > 0:
                    break

            inforeg["passwordPerson"] = input("Введите пароль: ")
            inforeg["namePerson"] = input("Введите имя: ")
            inforeg["surnamePerson"] = input("Введите фамилию: ")
            
            p = int(input("Подтвердить регистрацию?\n1 - Да\n2 - Отмена\n"))
            if p == 1:
                print("Вы зарегестрированы!")
                regList.append(inforeg)
                break  
            elif p == 2:
                print("Регистрация")
    elif vybor == 2:
        print("Вход")
        myLogin = input("Введите логин: ")
        myPassword = input("Введите пароль: ")
        for i in range(0,len(regList)):
            if myLogin == regList[i]["loginPerson"] and myPassword == regList[i]["passwordPerson"]:
                print("Вход совершен успешно!")
                while True:
                    vybor1 = int(input("Выберите действие\n1 - Просмотр информации\n2 - Выйти\n3 - Редактировать данные\n"))
                    if vybor1 == 1:
                            print(f"Имя - {regList[i]['namePerson']}")
                            print(f"Фамилия - {regList[i]['surnamePerson']}")
                            print(f"Логин - {regList[i]['loginPerson']}")
                    elif vybor1 == 2:
                        break
                    elif vybor1 == 3:
                        print("Редактирование данных")
                        reduct = int(input("1 - Имя\n2 - Фамилия\n3 - Пароль\n"))
                        if reduct == 1:
                            print(f"Ваше имя {regList[i]['namePerson']}")
                            regList[i]["namePerson"] = input("Введите новое имя: ")
                        elif reduct == 2:
                            print(f"Ваша фамилия {regList[i]['surnamePerson']}")
                            regList[i]["surnamePerson"] = input("Введите новую фамилию: ")
                        elif reduct == 3:
                            print(f"Ваш пароль {regList[i]['passwordPerson']}")
                            regList[i]["passwordPerson"] = input("Введите новый пароль: ")
                break
            elif len(userList) - 1 == i:
                print("Неверный логин или пароль")
        
        