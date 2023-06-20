#Задание 4 

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
reg = 0
while True:
    vybor = input("Выберите действие\n1 - Регистрация\n2 - Вход\n")
    if vybor == "1":
        print("Регистрация")
        myName = input("Введите имя: ")
        mySurname = input("Введите фамилию: ")
        myLogin = input("Введите логин: ")
        myPassword = input("Введите пароль: ")
        inforeg = {
        "namePerson" : myName,
        "surnamePerson" : mySurname,
        "loginPerson" : myLogin,
        "passwordPerson" : myPassword,
        }
        if myLogin == regList:
            print("Логин занят, введите другой!")
        else:
            p = input("Подтвердить регистрацию?\n1 - Да\n2 - Отмена\n")
            if p == "1":
                print("Вы зарегестрированы!")
                regList.append(inforeg)     
            elif p == "2":
                break
            else:
                print("Ошибка! Выберите действие")
    elif vybor == "2":
        print("Вход")
        myLogin = input("Введите логин: ")
        myPassword = input("Введите пароль: ")
        for i in range(0,len(regList)):
            if myLogin in regList[i]["loginPerson"] and myPassword in regList[i]["passwordPerson"]:
                print("Вход совершен успешно!")
                vybor1 = input("Выберите действие\n1 - Просмотр информации\n2 - Выйти\n3 - Редактировать данные\n")
                for i in range(0,len(regList)):
                    if vybor1 == "1":
                        print(f"Имя - {regList[i]['namePerson']}")
                        print(f"Фамилия - {regList[i]['surnamePerson']}")
                        print(f"Логин - {regList[i]['loginPerson']}")
                        reg = 0
                    elif vybor1 == "2":
                        break
                    elif vybor1 == "3":
                        print("Редактирование данных")
                        redName = input("Введите имя: ")
                        redSurname = input("Введите фамилию: ")
                        redPassword = input("Введите пароль: ")
                        if regList[i]["namePerson"] == myName or regList[i]["surnamePerson"] == mySurname or regList[i]["surnamePerson"] == myPassword:
                            regList[i]["namePerson"] = redName
                            regList[i]["surnamePerson"] = redSurname
                            regList[i]["passwordPerson"] = redPassword
                            print("Изменения сохранены!")
                        else:
                            print("Ошибка! Выберите действие")
            else:
                print("Неверный логин или пароль!")
    else:
        print("Ошибка! Выберите действие")
        

