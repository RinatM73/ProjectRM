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


genderList = ["Мужской", "Женский"]
raceList = ["Человек" , "Эльф" , "Гном" , "Орк"]
roleList = ["Воин","Лучник","Маг"]
textRace = ""
textGender = ""
# for i in range (0,len(genderList)):
#     textGender += f"{i} - {genderList[i]}\n"
# reg_gender = False
# while reg_gender == False:
#     myGender = int(input(f"Выберите пол:\n{textGender}"))
#     if i >= len(genderList) or myGender < 0:
#         print("Ошибка, выбери из перечисленного")
#     else:
#         for i in range ( 0 , len(genderList)):
#             if myGender == i:
#                 gender = genderList[i]
#                 reg_gender = True
#                 print("Вы выбрали", myGender)
#                 break
for i in range ( 0 , len(raceList)):
    textRace += f"{i} - {raceList[i]}\n"
reg_race = False # создали галочку
while reg_race == False: # выполнять пока False
    # принимает только число
    myRace = int(input(f"Выберите расу:\n{textRace}"))
    if i >= len(raceList) or myRace < 0:
        print("Ошибка, выбери из перечисленного")
    else:
        for i in range ( 0 , len(raceList)):
            if myRace == i:
                race = raceList[i]
                reg_race = True
                print("Вы выбрали", myRace)
                break
            
        # print(f"Я выбрал {raceList[myRace]} ПК сравнивает с {raceList[i]}")
