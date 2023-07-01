# # Задание 1

# numberList = [1,2,3,4,5,6,7,8,9,22,11,10,6,5,22]
# def delNumber(massiv):
#     print("вошел", massiv, "кол-во",len(massiv) )
#     for i in range(0,len(massiv)):
#         if i == len(massiv):
#             return massiv
#         elif massiv[i] % 2 == 0 :
#             massiv.pop(i)
#             print("вышел", massiv)
#             delNumber(massiv)
# delNumber(numberList)


# Задание 2

clientList = [
    {
        "myName" : "Александр",
        "status" : "Оплачен"
    },
    {
        "myName" : "Василий",
        "status" : "Не оплачен"
    },
    {
        "myName" : "Петр",
        "status" : "Оплачен"
    },
    {
        "myName" : "Арсений",
        "status" : "Не оплачен"
    },
    {
        "myName" : "Вадим",
        "status" : "Оплачен"
    },
    {
        "myName" : "Сергей",
        "status" : "Не оплачен"
    },
]
def neopl(massiv):
    print("Список")
    print("Количество: ", len(massiv))
    for i in range(0,len(massiv)):
        print(f"Имя: {clientList[i]['myName']} | Статус: {clientList[i]['status']}")
    for i in range(0,len(massiv)):
        if i == len(massiv):
            return massiv
        elif clientList[i]["status"] == "Не оплачен":
            massiv.pop(i)
            print("Список обновлен")
            print("Количество: ", len(massiv))
            for i in range(0,len(massiv)):
                print(f"Имя {clientList[i]['myName']} | Статус {clientList[i]['status']}")
            print("---------------------------------")
            neopl(massiv)
neopl(clientList)

