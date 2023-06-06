# Массивы

# v = 90
# t = 1
# s = v * t
#                 0          1
# genderList = ["Мужской", "Женский"]
# print(genderList[0])
# numberList = [3,1,4,3,6,7,3,5,1,9]
# numberList.sort()
# print(len(numberList))

# raceList = ["Человек","Эльф"]
# print(raceList)
# raceList.append("Гном")
# print(raceList, "raceList.append(\"Гном\")")
# raceList.pop(1)
# print(raceList, "raceList.pop(1)")
# raceList.clear()
# print(raceList, "raceList.clear()")

# numberList = [3,1,4,3,6,7,3,5,1,9]
# print(numberList)
# for i in range(0,len(numberList)):

#     # numberList[i] = numberList[i]**2
#     if numberList[i] % 2 != 0:
#         numberList.pop(i)
# print(numberList)

# listN = [[1,2,3,4,5],
#          [6,7,8,9,10],
# ]
# for i in range(0,len(listN)):
#     print(listN[i])
#     for j in range(0,len(listN[i])):
#         print(listN[i][j])

# 0 - переменные( массивы имеют окончание list)
# переменные должны быть названы за что отвечают, если это массив racelist  - список рас


# genderList = ["Мужской", "Женский"] # 0.1 - массив для определения персонажа
# raceList = ["Человек" , "Эльф" , "Гном" , "Орк"] # 0.2 - массив для определения рассы
# roleList = ["Воин","Лучник","Маг"] # 0.3 - массив для определения роли
# textRace = ""
# textGender = "" # 0.4 переменная для выводы всех возможных рас, изначально она пустая
# # for i in range (0,len(genderList)):
# #     textGender += f"{i} - {genderList[i]}\n"
# # reg_gender = False
# # while reg_gender == False:
# #     myGender = int(input(f"Выберите пол:\n{textGender}"))
# #     if i >= len(genderList) or myGender < 0:
# #         print("Ошибка, выбери из перечисленного")
# #     else:
# #         for i in range ( 0 , len(genderList)):
# #             if myGender == i:
# #                 gender = genderList[i]
# #                 reg_gender = True
# #                 print("Вы выбрали", myGender)
# #                 break
# for i in range ( 0 , len(raceList)): # повторять от 0 до количества рас
#     # в пустую строку каждый раз будет прописываться порядковый номер расы и его значение, к примеру вывод после 2 повторений будет выглядеть так
#     # № - значение
#     # 0 - Человек
#     # 1 - Эльф
#     # т.к.            № 0      №1
#     # raceList = ["Человек", "Эльф", "Гном", "Орк", "Тролль"]
#     textRace += f"{i} - {raceList[i]}\n"
# reg_race = False # создали галочку
# while reg_race == False: # выполнять пока False
#     # принимает только число
#     myRace = int(input(f"Выберите расу:\n{textRace}"))
#     if i >= len(raceList) or myRace < 0:
#         print("Ошибка, выбери из перечисленного")
#     else:
#         for i in range ( 0 , len(raceList)):
#             if myRace == i:
#                 race = raceList[i]
#                 reg_race = True
#                 print("Вы выбрали", myRace)
#                 break
            
#         print(f"Я выбрал {raceList[myRace]} ПК сравнивает с {raceList[i]}")


# # Саша и Маша собирают яблоки на компот, т.к. Саша сильнее Маши он должен собрать 6 яблок, а Маша должна собрать 3 яблока. Для компота нужно
# # 8 яблок. Обязательно чтобы Маша и  Саша принесли 8 яблок, 9е могут оставить себе.

# result = False # False - яблоки не собраны
# masha = 0 # количество собранных яблок
# sasha = 0 # количество собранных яблок
# # собирать яблоки пока у Маши и Саши не будет 8 шт
# while result == False:
#     sasha = int(input("Сколько яблок собрал Саша?: "))
#     if sasha <= 6: # если Саша собрал меньше чем 6 яблок, он должен продолжить собирать
#         print(f"Саша должен собрать еще {6 - sasha} яблока")
#     else:
#         print("Саша не может унести яблоки и все потерял")
#         sasha = 0
#     masha = int(input("Сколько яблок собрала Маша?: "))
#     if masha <= 3: # если Саша собрал меньше чем 6 яблок, он должен продолжить собирать
#         print(f"Маша должна собрать еще {3 - masha} яблока")
#     else:
#         print("Маша не может унести яблоки и все потерял")
#         masha = 0

# if masha + sasha >= 8:
#     result = True
#     print(f"Компот готов и осталось {(sasha+masha)-8} яблок")
        
# Гости

print("Регистрация гостей")
guestList = []
textGuest = ""
while True:
    vybor = input("Выберите действие\n1 - Добавить гостя\n2 - Удалить гостя\n3 - Просмотреть гостей")
    if vybor == "1":
        guest_name = input("Введите имя: ")
        guestList.append(guest_name)
    elif vybor == "2":
        guest_name = input("Введите имя: ")
        guestList.remove(guest_name)
    elif vybor == "3":
        print("Список гостей: ")
        print(f"{guestList}")
    elif vybor == "4":
        zc = input("Закончить приглашение?\n1 - Да\n2 - Нет")
        if zc == "1":
            print("Закончено")
        elif zc == "2":
    if 5 < vybor < 10:
        vybor = (1,2,3,4)
    else:
        vybor = (1,2,3)


        
