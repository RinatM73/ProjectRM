print("Регистрация гостей")
guestList = [] #создали пустой массив
while True:
    if len(guestList) <= 5: # если гостей до 5 включительно задаем три действия
        vybor = input("Выберите действие\n1 - Добавить гостя\n2 - Удалить гостя\n3 - Просмотреть список гостей\n> \n")
    else: # если гостей больше 5 задаем четыре действия
        vybor = input("Выберите действие\n1 - Добавить гостя\n2 - Удалить гостя\n3 - Просмотреть список гостей\n4 - Закончить приглашение?\n> \n")
    if vybor == "1":
        if len(guestList) < 10: # максимальное количество гостей 10
            guestName = input("Введите имя гостя: ")
            guestAge = int(input("Введите возраст гостя: "))
            infoGuest = {
                "guestName" : guestName,
                "guestAge" : guestAge,
            }     # создали объект
            if guestAge <= 10:  # создали условие при котором нельзя приглашать гостей
                print("Нельзя приглашать гостей младше 10 лет включительно!\n")
            else:
                guestList.append(infoGuest) # в противном случае гость добавляется в список
                print("Гость добавлен\n")
        else:
            print("Список гостей заполнен!")
    elif vybor == "2":
        if len(guestList) > 0:
            guestName = input("Введите имя гостя: ")
            guestAge = int(input("Введите возраст гостя: "))
            guestList.remove(infoGuest) # удаление введенного имени из списка гостей если список не пуст
            print("Гость удален\n")
        else:
            print("Список пуст!")
    elif vybor == "3":
        if len(guestList) > 0:
            textGuest = "" # создали пустую переменную для "взрослых"
            textGuest1 = "" # создали пустую переменную для "детей"
            print("Список гостей: ")
            n = 0 # создали счетчик для нумерации гостей
            for i in range(0,len(guestList)): #создаем цикл для просмотра списка гостей("Взрослые")
                if guestList[i]['guestAge'] >= 18:
                    n = n + 1 # добавляем единицу к порядковому номеру каждого следующего гостя
                    textGuest += f"{n} - Имя: {guestList[i]['guestName']}\n    Возраст: {guestList[i]['guestAge']}\n" 
            print("Взрослые:\n")
            print(textGuest) # вывод списка гостей("Взрослые") если он не пуст
            for i in range(0,len(guestList)): #создаем цикл для просмотра списка гостей("Дети")
                if guestList[i]['guestAge'] < 18:
                    n = n + 1 # добавляем единицу к порядковому номеру каждого следующего гостя
                    textGuest1 += f"{n} - Имя: {guestList[i]['guestName']}\n    Возраст: {guestList[i]['guestAge']}\n" 
            print("Дети:\n")
            print(textGuest1) # вывод списка гостей("Дети") если он не пуст
        else:
            print("Список пуст!")
    elif vybor == "4":
        if 5 < len(guestList) < 10: # заканчиваем цикл по запросу, если число гостей больше 5 и меньше 10
            break