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