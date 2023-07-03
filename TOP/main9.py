# Делегирование, мышление ООП.



# Двигатель и его функции
def start():
    print("Запуск")

def stop():
    print("Стоп")

Engine = {
    "start" : start,
    "stop" : stop,
}

# Engine["start"]()
# Engine["stop"]()
def open():
    print("Капот открыт")

def close():
    print("Капот закрыт")

Bonnet = {
    "open" : open,
    "close" : close,
}

# Основа авто
Car = {
    "color" : "",
    "marka" : "",
    "Engine" : "",
    "Bonnet" : ""
}

auto = Car
auto["marka"] = "audi"
auto["color"] = "green"
auto["Engine"] = Engine
print(auto)
auto["Engine"]["start"]()



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

# import copy
# # Создание персонажа
# def attack(param):
#     print(param)

# def shoot():
#     print("Выстрел")

# Person = {
#     "name" : "Варвар",
#     "gender" : "Мужской",
#     "actions" : {
#         "attack" : attack
#     }
# }
# # Создание расы на основе объекта
# Human = copy.deepcopy(Person)
# Human["race"] = "Человек"
# Human["skills"] = ["Быстрый бег", "Красноречие"]


# Orc = copy.deepcopy(Person)
# Orc["race"] = "Орк"
# Orc["skills"] = ["Сила", "Быстрый бег"]

# # Создание ролей на основе race

# Warrior = copy.deepcopy(Human) or copy.deepcopy(Orc)
# Warrior["role"] = "Воин"
# Warrior["desc"] = "Воин отличается своим сочетанием мобильности и живучести"
# Warrior["actions"]["attack"]("удар")

# Archer = copy.deepcopy(Human)
# Archer["role"] = "Лучник"
# Archer["desk"] = "Способны избегать все эффекты контроля"
# Archer["actions"]["attack"]("стрельба")

# Shaman = copy.deepcopy(Orc)
# Shaman["role"] = "Шаман"
# Shaman["desk"] = "Наставники в духовных практиках"
# Shaman["ataka"] = "заклинание"
# Shaman["actions"]["attack"] = attack(Shaman["ataka"])

# print("--------------")
# print(Person)
# print("--------------")
# print(Human)
# print("--------------")
# print(Orc)
# print("--------------")
# print(Warrior)
# print("--------------")
# print(Archer)
# print("--------------")
# print(Shaman)

# myPerson = copy.deepcopy(Shaman)
# myPerson["actions"]["attack"]


# Классы


# class Car:
#     def __init__(self, color, marka, engine, cond, light, wheels): # создание переменных для класса(объекта)
#         self.color = color
#         self.marka = marka
#         self.engine = engine
#         self.cond = cond
#         self.light = light
#         self.wheels = wheels
#     # методы - действия с определенным классом
#     def showColor(self):
#         print(self.color)

#     def showHP(self):
#         print("Наследуется")
# class Engine:
#     def __init__(self, HP, volume, turbo):
#         self.HP = HP
#         self.volume = volume
#         self.turbo = turbo

#     def start(self):
#         print("Запуск")
    
#     def stop(self):
#         print("Стоп")

# class Cond:
#     def __init__(self, gradleft, gradright):
#         self.gradleft = gradleft
#         self.gradright = gradright

#     def start(self):
#         print("Запуск кондиционера")

#     def stop(self):
#         print("Стоп")

# class Light:

#     def startlow(self):
#         print("Вкл фары ближний")

#     def stoplow(self):
#         print("Выкл фары ближний")

#     def starthigh(self):
#         print("Вкл фары дальний")

#     def stophigh(self):
#         print("Выкл фары дальний")

# class Wheels:
#     def __init__(self, width, height, diametr):
#         self.width = width
#         self.height = height
#         self.diametr = diametr

#     def turnleft(self):
#         print("Повернуть налево")

#     def turnright(self):
#         print("Повернуть направо")

# myEngine = Engine(120,2)
# twoEngine = Engine(280,2.2)
# myCond = Cond(25,27)
# myLight = Light()
# myWheels = Wheels(225,45,17)
# myAuto = Car("green","audi",myEngine,myCond,myLight,myWheels)
# myAuto.cond.start()
# myAuto.light.starthigh()
# myAuto.wheels.turnleft()
# print(myAuto.engine.HP)

# # Наследование

# class SportCar(Car):
#     def __init__(self, color, marka, engine, cond, light, wheels):
#         # self.color = color
#         # self.marka = marka
#         # self.engine = engine
#         # self.cond = cond
#         # self.light = light
#         # self.wheels = wheels
#         super().__init__(color, marka, engine, cond, light, wheels)

# class EngineSuper(Engine):
#     def __init__(self, HP, volume, turbo)
#         self.coldfilter = coldfilter



# lamborginiEngine = Engine(900, 6)
# twoAuto = SportCar("blue","lamborgini", lamborginiEngine,cond, light, wheels, 2)






# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound

#     def activeSound(self):
#         print(self.sound)

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name, "Мяу!")

#     def purr(self):
#         print("Мурлыкает")

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name, "Гав!")

#     def digHole(self):
#         print("Копает яму")

# myCat = Cat("Вася")
# myCat.activeSound()

