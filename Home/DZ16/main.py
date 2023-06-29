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
                myLogin = input("Введите имя: ")
                if len(regList) > 0:
                    for i in range(0,len(regList)):
                        if myLogin != userList[i]["loginPerson"]:
                            inforeg["loginPerson"] = myLogin
                        elif len(regList) - 1 == i:
                            print("Логин занят, введите другой!")
                            inforeg["loginPerson"] = ""
                            break
                else:
                    inforeg["loginPerson"] = myLogin
                if len(regList["loginPerson"]) > 0:
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
    elif vybor == "2":
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
                        reduct = int(input("1 - Имя\n2 - Фамилия\n3 - Пароль"))
                        if reduct == 1:
                            print(f"Ваше имя {regList['namePerson']}")
                            regList["namePerson"] = input("Введите новое имя: ")
                        elif reduct == 2:
                            print(f"Ваша фамилия {regList['surnamePerson']}")
                            regList["surnamePerson"] = input("Введите новую фамилию: ")
                        elif reduct == 3:
                            print(f"Ваш пароль {regList['passwordPerson']}")
                            regList["passwordPerson"] = input("Введите новый пароль: ")
                break
            elif len(userList) - 1 == i:
                print("Неверный логин или пароль")
        



# userList = []
# while True:
#     x = int(input("Выбор:\n1 - Регистрация нового пользователя\n2 - Вход в личный кабинет"))
#     if x == 1: # цикл для регистрации нового пользователя
#         print("---- Регистрация ----")
#         while True:
#             regUser = {
#                 "userLogin" : "",
#                 "userPassword" : "",
#                 "userName" : "",
#                 "userFirstName" : "",
#             }
#             while True:
#                 regLogin = input("Введите логин: ")
#                 if len(userList) > 0:
#                     for i in range(0,len(userList)):
#                         if regLogin != userList[i]["userLogin"]:
#                             regUser["userLogin"] = regLogin
#                         elif len(userList) - 1 == i:
#                             print("Данный логин уже занят\nвведите другой")
#                             regUser["userLogin"] = ""
#                             break
#                 else:
#                     regUser["userLogin"] = regLogin
#                 if len(regUser["userLogin"]) > 0:
#                     break
#             regUser["userPassword"] = input("Введите пароль нового пользователя: ")
#             regUser["userName"] = input("Введите имя нового пользователя: ")
#             regUser["userFirstName"] = input("Введите фамилию нового пользователя: ")
#             print("Регистрация завершена")
#             check = int(input("1 - подтвердить\n2 - ввести данные снова"))
#             if check == 1:
#                 userList.append(regUser)
#                 break
#             elif check == 2:
#                 print("---- Регистрация ----")
#     elif x == 2:
#         print("-- Вход в ЛК")
#         inLogin = input("Введите логин: ")
#         inPassword = input("Введите пароль: ")
#         for i in range(0,len(userList)):
#             if inLogin == userList[i]["userLogin"] and inPassword == userList[i]["userPassword"]:
#                 print("Вход выполнен")
#                 while True:
#                     infoUser = int(input("1 - Посмотреть информацию\n2 - Редактировать информацию\n3 - Выход"))
#                     if infoUser == 1:
#                         print(f'Имя : {userList[i]["userName"]}\n',
#                               f'Фамилия : {userList[i]["userFirstName"]}\n',
#                               f'Логин : {userList[i]["userLogin"]}\n',
#                               f'Пароль : {userList[i]["userPassword"]}\n')
#                     elif infoUser == 2:
#                         print("Редактирование данных")
#                         upDate = int(input("1 - Имя\n2 - Фамилия\n3 - Пароль"))
#                         if upDate == 1:
#                             print(f'Ваше имя {userList[i]["userName"]}')
#                             userList[i]["userName"] = input("Новое имя:")
#                         elif upDate == 2:
#                             print(f'Ваша фамилия {userList[i]["userFirstName"]}')
#                             userList[i]["userFirstName"] = input("Новая фамилия:")
#                         elif upDate == 3:
#                             print(f'Ваш пароль {userList[i]["userPassword"]}')
#                             userList[i]["userPassword"] = input("Новый пароль:")
#                     elif infoUser == 3:
#                         break

#                 break
#             elif len(userList) - 1 == i:
#                 print("Неверный логин или пароль")
        