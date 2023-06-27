# Делегирование, мышление ООП.



# # Двигатель и его функции
# def start():
#     print("Запуск")

# def stop():
#     print("Стоп")

# Engine = {
#     "start" : start,
#     "stop" : stop,
# }

# # Engine["start"]()
# # Engine["stop"]()
# def open():
#     print("Капот открыт")

# def close():
#     print("Капот закрыт")

# Bonnet = {
#     "open" : open,
#     "close" : close,
# }

# # Основа авто
# Car = {
#     "color" : "",
#     "marka" : "",
#     "Engine" : "",
#     "Bonnet" : ""
# }

# auto = Car
# auto["marka"] = "audi"
# auto["color"] = "green"
# auto["Engine"] = Engine
# # print(auto)
# auto["Engine"]["start"]()



# # Основная функция
# def Car(marka,color):
#     thisMarka = marka
#     thisColor = color

#     activeList = {
#         "showMarka" : showMarka
#     }
    
# def showMarka(param):
#     print(param)

# auto = Car("audi","green")

# Mash = {
#     "color" : "",
#     "marka" : ""
# }

# Car = Mash.copy
# Car["Engine"] = Engine
# Car["Doors"] = "двери"

# myAuto = Car
# myAuto["color"] = "Синий"

# Ster = Mash

# Ster["Engine"] = Engine
# Ster["Baraban"] = "Барабан"
# mySter = Ster
# mySter["color"] = "Белый"

#-----------------------------------------------

import copy
# Создание персонажа
def attack(param):
    print(param)

def shoot():
    print("Выстрел")

Person = {
    "name" : "Варвар",
    "gender" : "Мужской",
    "actions" : {
        "attack" : attack
    }
}
# Создание расы на основе объекта
Human = copy.deepcopy(Person)
Human["race"] = "Человек"
Human["skills"] = ["Быстрый бег", "Красноречие"]


Orc = copy.deepcopy(Person)
Orc["race"] = "Орк"
Orc["skills"] = ["Сила", "Быстрый бег"]

# Создание ролей на основе race

Warrior = copy.deepcopy(Human) or copy.deepcopy(Orc)
Warrior["role"] = "Воин"
Warrior["desc"] = "Воин отличается своим сочетанием мобильности и живучести"
Warrior["actions"]["attack"]("удар")

Archer = copy.deepcopy(Human)
Archer["role"] = "Лучник"
Archer["desk"] = "Способны избегать все эффекты контроля"
Archer["actions"]["attack"]("стрельба")

Shaman = copy.deepcopy(Orc)
Shaman["role"] = "Шаман"
Shaman["desk"] = "Наставники в духовных практиках"
Shaman["ataka"] = "заклинание"
Shaman["actions"]["attack"] = attack(Shaman["ataka"])

print("--------------")
print(Person)
print("--------------")
print(Human)
print("--------------")
print(Orc)
print("--------------")
print(Warrior)
print("--------------")
print(Archer)
print("--------------")
print(Shaman)

myPerson = copy.deepcopy(Shaman)
myPerson["actions"]["attack"]


