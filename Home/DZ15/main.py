print("Регистрация гостей")
guestList = []
while True:
    if len(guestList) <= 5: # если гостей до 5 включительно задаем три действия
        vybor = input("Выберите действие\n1 - Добавить гостя\n2 - Удалить гостя\n3 - Просмотреть список гостей\n> ")
    else: # если гостей больше 5 задаем четыре действия
        vybor = input("Выберите действие\n1 - Добавить гостя\n2 - Удалить гостя\n3 - Просмотреть список гостей\n4 - Закончить приглашение?\n> ")
    if vybor == "1":
        if len(guestList) < 10: # максимальное количество гостей 10
            guestName = input("Введите имя гостя: ")
            guestAge = int(input("Введите возраст гостя: "))
            infoGuest = {
                "guestName" : guestName,
                "guestAge" : guestAge,
                "guestReb" : ""
            }
            if guestAge <= 10:
                print("Нельзя приглашать гостей младше 10 лет включительно!\n")
            else:
                guestList.append(infoGuest)
                print("Гость добавлен\n")
            for i in range(0,len(guestList)):
                if guestAge < 18:
                    guestList[i] = x
                else:
                    guestList[i] = y
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
            textGuest = ""
            print("Список гостей: ")
            for i in range(0,len(guestList)): #создаем цикл для просмотра списка гостей
                textGuest += f"{i + 1} - Имя: {guestList[i]['guestName']}\n    Возраст: {guestList[i]['guestAge']}\n" 
                # плюсуем к i единицу для того чтобы в выведенном списке отсчет начинался от 1, а не от 0
            print(textGuest) # вывод списка гостей если он не пуст
        else:
            print("Список пуст!")
    elif vybor == "4":
        if 5 < len(guestList) < 10: # заканчиваем цикл по запросу, если число гостей больше 5 и меньше 10
            break