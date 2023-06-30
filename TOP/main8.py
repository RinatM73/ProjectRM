def menu(massiv):
    print(massiv)

def newMenu(massiv):
    for i in range(0,len(massiv)):
        print(massiv[i]["name"])

def x(massiv):
    listMenu = [
        {
            "nameFunc" : "Функция показа списка",
            "startFunc" : menu(massiv)
        },
        {
            "nameFunc" : "Показать имя объекта",
            "startFunc" : newMenu(massiv)
        }
    ]
    text = ""
    for i in range(0,len(listMenu)):
        text += f'{i} - {listMenu[i]["nameFunc"]}\n'
    print(text)
    x = int(input("Введите"))
    for i in range(0,len(listMenu)):
        if x == i:
            listMenu[i]["startFunc"]


arrMass = [
    {
        "name" : "Макс"
    },
    {
        "name" : "Денис"
    }
]



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