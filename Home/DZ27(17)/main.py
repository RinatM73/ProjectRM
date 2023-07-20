print("Регистрация гостей")
guestList = []
blackList = ["Костя", "Федя", "Петя"]
while True:
    if len(guestList) <= 5: # если гостей до 5 включительно задаем три действия
        vybor = input("Выберите действие\n1 - Добавить гостя\n2 - Удалить гостя\n3 - Просмотреть список гостей\n> ")
    else: # если гостей больше 5 задаем четыре действия
        vybor = input("Выберите действие\n1 - Добавить гостя\n2 - Удалить гостя\n3 - Просмотреть список гостей\n4 - Закончить приглашение?\n> ")
    if vybor == "1":
        if len(guestList) < 10: # максимальное количество гостей 10
            guest_name = input("Введите имя: ")
            if guest_name not in blackList: # если введенное имя не присутствует в черном списке, то добавляем его в список гостей
                guestList.append(guest_name) # добавление введенного имени в список гостей
            else: # в противном случай имя не добавляется
                print("Данный гость в черном списке!")
        else:
            print("Список гостей заполнен!")
    elif vybor == "2":
        if len(guestList) > 0:
            guest_name = input("Введите имя: ")
            guestList.remove(guest_name) # удаление введенного имени из списка гостей если список не пуст
        else:
            print("Список пуст!")
    elif vybor == "3":
        if len(guestList) > 0:
            textGuest = ""
            print("Список гостей: ")
            for i in range(0,len(guestList)): #создаем цикл для просмотра списка гостей
                textGuest += f"{i + 1} - {guestList[i]}\n" # плюсуем к i единицу для того чтобы в выведенном списке отсчет начинался от 1, а не от 0
            print(textGuest) # вывод списка гостей если он не пуст
        else:
            print("Список пуст!")
    elif vybor == "4":
        if 5 < len(guestList) < 10: # заканчиваем цикл по запросу, если число гостей больше 5 и меньше 10
            break

import json

def globalReg():
    if len(guestList) <= 5: # если гостей до 5 включительно задаем три действия
        vybor = int(input("Выберите действие\n1 - Добавить гостя\n2 - Удалить гостя\n3 - Просмотреть список гостей\n> "))
    else: # если гостей больше 5 задаем четыре действия
        vybor = int(input("Выберите действие\n1 - Добавить гостя\n2 - Удалить гостя\n3 - Просмотреть список гостей\n4 - Закончить приглашение?\n> "))
    if vybor == 1:
        guestAdd()
    elif vybor == 2:
        guestDel()
    elif vybor == 3:
        listShow()
    else:
        break

def guestAdd():
    if len(guestList) < 10: # максимальное количество гостей 10
        guest_name = input("Введите имя: ")
        if guest_name not in blackList: # если введенное имя не присутствует в черном списке, то добавляем его в список гостей
            base_list = open("base.json","r",encoding="utf-8")
            base_list_read = base_list.read()
            new_base = json.loads(base_list_read) # из строки сделали массив
            new_base.append({
                    "guest_name" : guest_name
            }) # добавление введенного имени в список гостей
        else: # в противном случай имя не добавляется
            print("Данный гость в черном списке!")
    else:
        print("Список гостей заполнен!")

def guestDel():
    if len(guestList) > 0:
        guest_name = input("Введите имя: ")
        guestList.remove(guest_name) # удаление введенного имени из списка гостей если список не пуст
    else:
        print("Список пуст!")

def listShow():
    if len(guestList) > 0:
            textGuest = ""
            print("Список гостей: ")
            for i in range(0,len(guestList)): #создаем цикл для просмотра списка гостей
                textGuest += f"{i + 1} - {guestList[i]}\n" # плюсуем к i единицу для того чтобы в выведенном списке отсчет начинался от 1, а не от 0
            print(textGuest) # вывод списка гостей если он не пуст
    else:
        print("Список пуст!")
