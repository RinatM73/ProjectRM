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
# print(auto)
# auto["Engine"]["start"]()
# auto["Bonnet"]["open"]()


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

# myEngine = Engine(120,2,1)
# # twoEngine = Engine(280,2.2)
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


# Абстрактные классы


# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
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

# class Donkey(Animal):
#     def __init__(self, name):
#         super().__init__(name, "Иа-иа")


# myCat = Cat("Вася")
# myCat.activeSound()

# myDonkey = Donkey("Осел")
# myDonkey.activeSound()







# from abc import ABC, abstractmethod

# class Human(ABC):
#     @abstractmethod
#     def __init__(self, name, nationality):
#         self.name = name
#         self.nationality = nationality
#         print(self.gender)

# class Man(Human):
#     def __init__(self, name, nationality):
#         self.gender = "Мужской"
#         super().__init__(name, nationality)

# class Woman(Human):
#     def __init__(self, name, nationality):
#         self.gender = "Женский"
#         super().__init__(name, nationality)

# baby = Man("Денис", "Китаец")








# from abc import ABC, abstractmethod

# class Grandfather(ABC):
#     @abstractmethod
#     def __init__(self, name, hairColor):
#         self.name = name
#         self.hairColor = hairColor
    
#     def cookingBorscht(self):
#         print("Готовил вкусный борщ")

#     def repairCar(self):
#         print("Ремонтировал авто")

# class Father(Grandfather, ABC):
#     @abstractmethod
#     def __init__(self, name, hairColor):
#         super().__init__(self, name, hairColor)

# Ilya = Grandfather("Илья", "Русый")
# Ilya.cookingBorscht()

# Michael = Father("Михаил", "Русый")
# Michael = cookingBorscht()







# class Bird():

#     def __init__(self, name, sound) -> None:
#         self.name = name
#         self.sound = sound

#     def eat(self):
#         print("Кушает")

#     def hunting(self):
#         print("Охотятся")

#     def activeSound(self):
#         print(self.sound)

# class noFly(Bird):

#     def __init__(self, name, sound="") -> None:
#         super().__init__(name, sound)

#     def goes(self):
#         print("Ходит")

# class flyBird(noFly):

#     def __init__(self, name, sound="") -> None:
#         super().__init__(name, sound)

#     def fly(self):
#         print("Летает")

# class Crow(flyBird):

#     def __init__(self, name) -> None:
#         super().__init__(name, "Кар!")

# crow = Crow("Гриша")
# crow.activeSound()







base_list = [
    {
        "first_name" : "Денис",
        "last_name" : "Кириллов",
        "birthday" : "01.06.2001",
        "gender" : "Мужской",
        "login" : "denis161",
        "password" : "12345"
    },
    {
        "first_name" : "Кирилл",
        "last_name" : "Кириллов",
        "birthday" : "17.08.2006",
        "gender" : "Мужской",
        "login" : "kirillooo",
        "password" : "12345"
    },
    {
        "first_name" : "Максим",
        "last_name" : "Максимович",
        "birthday" : "01.06.2006",
        "gender" : "Мужской",
        "login" : "maks07",
        "password" : "12345"
    },
    {
        "first_name" : "Руслан",
        "last_name" : "Русланов",
        "birthday" : "01.06.2000",
        "gender" : "Мужской",
        "login" : "russlan",
        "password" : "12345"
    },
    {
        "first_name" : "Екатерина",
        "last_name" : "Исаева",
        "birthday" : "25.10.2000",
        "gender" : "Женский",
        "login" : "ekaterina25",
        "password" : "12345"
    },

]
registered_users = [

]

class User():
    def __init__(self, user_id, first_name, last_name, birthday, gender, login, password) -> None:
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.login = login
        self.password = password
        #-------------------------
        self.status = "user"
        self.blocking = False

    # Если в классе есть методы со словом update, значит этот метод для изменения информации
    def update_first_name(self, new_first_name):
        self.first_name = new_first_name

    def update_last_name(self, new_last_name):
        self.last_name = new_last_name
    
    def update_birthday(self, new_birthday):
        self.birthday = new_birthday

    def update_gender(self, new_gender):
        self.gender = new_gender

    def update_password(self, new_password):
        if self.password == input("Введите старый пароль: "):
            self.password = new_password

class Moderator(User):
    def __init__(self, user_id, first_name, last_name, birthday, gender, login, password):
        super().__init__(self, user_id, first_name, last_name, birthday, gender, login, password)
        self.status = "moderator"

    # создаем функцию блокировки списка юзеров
    def blocking_user(self, user_list):
        text_user_list = f"id | first_name | blocking | status \n"
        for i in range(0,len(user_list)):
            text_user_list += f"{i} - {user_list[i]['user_id']}{user_list[i]['first_name']} - {user_list[i]['blocking']} {user_list[i]['status']}\n"
        print(text_user_list)
        input_user_id = int(input("Введите id пользователя для блокировки: "))
        for i in range(0,len(user_list)):
            if self.status == "moderator":
                if input_user_id == i and user_list[i]['status'] != "moderator" and user_list[i]['status'] != "admin":
                    if user_list[i]['blocking'] == True:
                        print("Пользователь уже заблокирован")
                        break
                    else:
                        user_list[i]['blocking'] = True
                        print("Пользователь успешно заблокирован")
                        break
            elif self.status == "admin":
                if input_user_id == i:
                    if user_list[i]['blocking'] == True:
                        print("Пользователь уже заблокирован")
                        break
                    else:
                        user_list[i]['blocking'] = True
                        print("Пользователь успешно заблокирован")
                        break

class Admin(Moderator):
    def __init__(self, user_id, first_name, last_name, birthday, gender, login, password):
        super().__init__(self, user_id, first_name, last_name, birthday, gender, login, password)
        self.status = "admin"
    
    def delete_user_list(self, user_list):
        user_list.clear()
        print("База данных пуста")

    def create_user_list(self, massiv, user_list):   # massiv - массив данных
        for i in range(0,len(massiv)):
            user_list.append(User(user_id=i,
                                first_name = massiv[i]["first_name"],
                                last_name = massiv[i]["last_name"],
                                birthday = massiv[i]["birthday"],
                                gender = massiv[i]["gender"],
                                login = massiv[i]["login"],
                                password = massiv[i]["password"]))

myAdmin = Admin(10, "admin", "admin", "01.01.1970", "Мужской", "admin", "admin")
myAdmin.create_user_list(base_list,registered_users)
print(registered_users)
