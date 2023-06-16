#Функции


# def reg(x): 
#     print(x)

# reg(input("Введите имя: ")) #x = input("Введите свое имя: ")



# def f1(a,b):
#     print(a*b)
# f1(10,2)
# f1(5,9)


def regName(myName):
    print(myName)
    globalReg()
def regGender():
    listGender = ["муж","жен"]
    textGender = ""
    for i in range(0,len(listGender)):
        textGender += f"{i} - {listGender[i]}\n"
    myGender = int(input(f"{textGender}"))
    for i in range(0,len(listGender)):
        if myGender == i:
            myGender = listGender[i]
            break
    globalReg()

def globalReg():
    print("Регистрация персонажа")
    x = int(input("Выбор действия:\n1 - Ввод имени\n2 - Выбор гендера\n3 - Выбор расы"))
    if x == 1:
        regName(input("Введите имя персонажа"))
    elif x == 2:
        regGender()
    elif x == 3:
        regRace()

def regRace():
    listRace = ["Человек","Эльф","Гном"]
    textRace = ""
    for i in range(0,len(listRace)):
            textRace += f"{i} - {listRace[i]}\n"
    myRace = int(input(f"{textRace}"))
    for i in range(0,len(listRace)):
        if myRace == i:
            myRace = listRace[i]
            break  
    globalReg()
globalReg()
# def regRace():
#     pass