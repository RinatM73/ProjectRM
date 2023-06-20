#Функции


# def reg(x): 
#     print(x)

# reg(input("Введите имя: ")) #x = input("Введите свое имя: ")



# def f1(a,b):
#     print(a*b)
# f1(10,2)
# f1(5,9)


# def regName(myName):
#     print(myName)
#     globalReg()
# def regGender():
#     listGender = ["муж","жен"]
#     textGender = ""
#     for i in range(0,len(listGender)):
#         textGender += f"{i} - {listGender[i]}\n"
#     myGender = int(input(f"{textGender}"))
#     for i in range(0,len(listGender)):
#         if myGender == i:
#             myGender = listGender[i]
#             break
#     globalReg()

# def globalReg():
#     print("Регистрация персонажа")
#     x = int(input("Выбор действия:\n1 - Ввод имени\n2 - Выбор гендера\n3 - Выбор расы"))
#     if x == 1:
#         regName(input("Введите имя персонажа"))
#     elif x == 2:
#         regGender()
#     elif x == 3:
#         regRace()

# def regRace():
#     listRace = ["Человек","Эльф","Гном"]
#     textRace = ""
#     for i in range(0,len(listRace)):
#             textRace += f"{i} - {listRace[i]}\n"
#     myRace = int(input(f"{textRace}"))
#     for i in range(0,len(listRace)):
#         if myRace == i:
#             myRace = listRace[i]
#             break  
#     globalReg()
# globalReg()
# def regRace():
#     pass

# return

# def f1(a):
#     c = a - 50
#     print(f"Экран: ваша сдача {c}")
#     return c
# print(f"Вы получили на руки {f1(100)}")




# def regName(myName):
#     return name
    
# def regGender():
#     listGender = ["муж","жен"]
#     textGender = ""
#     for i in range(0,len(listGender)):
#         textGender += f"{i} - {listGender[i]}\n"
#     myGender = int(input(f"{textGender}"))
#     for i in range(0,len(listGender)):
#         if myGender == i:
#             return listGender[i]

# def globalReg():
#     x = int(input("1 - ввод имени\n2 - выбор пола"))
#     if x == 1:
#         myName = regName(input("ваше имя: "))
#         globalReg()
#     elif x == 2:
#         myGender = regGender()
#     return([myName,myGender])

# print(globalReg())




# myInfo = {

# }
# print(myInfo)
#           # myInfo
# def regName(massiv,newName):
#     print("в функцию пришло значение",massiv)
# #   myInfo["myName"] = newName
#     massiv["myName"] = newName
#     print("из функции отправили",massiv)
#     return massiv

# def regGender(massiv):
#     x = int(input("1-м\n2-ж"))
#     if x == 1:
#         massiv["myGender"] = "м"
#     elif x == 2:
#         massiv["myGender"] = "ж"
#     print("из функции отправили",massiv)
#     return massiv

# def globalReg(massiv):
#     # massiv = myInfo
#     x = int(input("1 - ввод имени\n2 - выбор пола\n"))
#     if x == 1:
#         regName(massiv)
#         regGender(massiv)
#     elif x == 2:
#         myGender = regGender(massiv)
#         globalReg(myGender)
#     return massiv

# newInfo = globalReg(myInfo)
# print(newInfo)


# Задание 1

def globalReg(x,y,z):
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    z = int(input("Введите третье число: "))
    d = int(input("Выберите действие 1 - сумма чисел\n2 - произведение чисел\n"))
    if d == 1:
        regSumma()
    elif d == 2:
        regProizv()

def regSumma(x,y,z):
    a = x + y + z
    print("Сумма чисел\n")
    print(a)
    return a
    globalReg()

def regProizv(x,y,z):
    b = x * y * z
    print("Произведение чисел\n")
    print(b)
    return b
    globalReg()
globalReg(x,y,z)