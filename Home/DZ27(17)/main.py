import json

base_list = []
blackList = []

def globalReg():

    if len(base_list) <= 5: # если гостей до 5 включительно задаем три действия
        vybor = int(input("Выберите действие\n1 - Добавить гостя\n2 - Удалить гостя\n3 - Просмотреть список гостей\n> "))
    else: # если гостей больше 5 задаем четыре действия
        vybor = int(input("Выберите действие\n1 - Добавить гостя\n2 - Удалить гостя\n3 - Просмотреть список гостей\n4 - Закончить приглашение?\n> "))
    if vybor == 1:
        guestAdd()
    elif vybor == 2:
        guestDel()
    elif vybor == 3:
        listShow()

def guestAdd():

    if len(base_list) < 10: # максимальное количество гостей 10
        guest_name = input("Введите имя: ")
        if guest_name not in blackList: # если введенное имя не присутствует в черном списке, то добавляем его в список гостей
            base_list.append(guest_name) # добавление введенного имени в список гостей
        else: # в противном случай имя не добавляется
            print("Данный гость в черном списке!")
    else:
        print("Список гостей заполнен!")

    with open('guests.json','w', encoding='utf-8') as f: #открываем файл для записи
        json.dump(base_list, f, ensure_ascii=False) #запись в формате json
    globalReg()

def guestDel():

    if len(base_list) > 0:
        guest_name = input("Введите имя: ")
        blackList.append(guest_name) # добавление введенного имени в черный список
        base_list.remove(guest_name) # удаление введенного имени из списка гостей

    else:
        print("Список пуст!")

    with open('black.json','w', encoding='utf-8') as f1: #открываем файл для записи
        json.dump(blackList, f1, ensure_ascii=False) #запись в формате json

    with open('guests.json','w', encoding='utf-8') as f3: #открываем файл для записи
        json.dump(base_list, f3, ensure_ascii=False) #запись в формате json

    globalReg()

def listShow():
    
    if len(base_list) > 0:
        textGuest = ""
        print("Список гостей: ")
        for i in range(0,len(base_list)): #создаем цикл для просмотра списка гостей
            textGuest += f"{i + 1} - {base_list[i]}\n" # плюсуем к i единицу для того чтобы в выведенном списке отсчет начинался от 1, а не от 0
            print(textGuest) # вывод списка гостей если он не пуст
    else:
        print("Список пуст!")
    globalReg()
globalReg()