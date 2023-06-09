# Объекты
#                0        1
# productList = ["Каша", "Вода"]
# print(productList[0])
# infoProduct = {
#     "nameProduct" : "Каша",
#     "price" : 120,
#     "sale" : "20%",
# }
# print(f"{infoProduct['price']}\n{infoProduct['sale']}")

# myName = input("Введите свое имя")
# myAge = input("Сколько вам лет?")
# infoPerson = {
#     "namePerson" : "Ринат",
#     "agePerson" : 22,
#     "hobbyPerson" : ["Sport", "Programming"]
# }
# print(infoPerson)

# for key in infoPerson:
#     print(f"{key} - {infoPerson[key]}")

# print(f"Имя: {infoPerson['namePerson']}")

# productList = [
#     {
#         "nameProduct" : "Хлеб",
#         "price" : 55,
#         "count" : 37,
#         "category" : "Хлебобулочная",
#     },
#     {
#         "nameProduct" : "Молоко",
#         "price" : 101,
#         "count" : 20,
#         "category" : "Молочная",
#     },
#     {
#         "nameProduct" : "Кефир",
#         "price" : 99,
#         "count" : 6,
#         "category" : "Молочная",
#     },
# ]
# for i in range(0,len(productList)):
#     if productList[i]["category"] == "Молочная":
#         productList[i]["price"] = productList[i]["price"] * 2
#         print(f"Название товара - {productList[i]['nameProduct']}")
#         print(f"Цена - {productList[i]['price']}")
#         print(f"Количество - {productList[i]['count']}")
#         print("--------------------------")

# Добавление объектов в пустые массивы

guestList = []
while True:
    nameGuest = input("Введите имя гостя: ")
    ageGuest = int(input("Введите возраст гостя: "))
# выше созданные переменные будут добавляться в объект infoGuest и вставляться в соответсвующие ключи
# infoGuest - хранит данные гостя
    infoGuest = {
        "nameGuest" : nameGuest,
        "ageGuest" : ageGuest,
    }
    guestList.append(infoGuest)
    if len(guestList) > 3:
        break

for i in range(0,len(guestList)):
    print(f"Имя гостя - {guestList[i]['nameGuest']}")
    print(f"Возраст гостя - {guestList[i]['ageGuest']}")
    print("-------------------")
