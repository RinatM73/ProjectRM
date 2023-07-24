import json


def globalReg():
    base_list = open("base.json","r",encoding="utf-8")
    base_list_read = base_list.read()
    new_base = json.loads(base_list_read) # из строки сделали массив
    base_list_read.close()
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
globalReg()

def guestAdd():
    base_list = open("base.json","r",encoding="utf-8")
    base_list_read = base_list.read()
    new_base = json.loads(base_list_read) # из строки сделали массив
    base_list_read.close()
    if len(base_list) < 10: # максимальное количество гостей 10
        guest_name = input("Введите имя: ")
        blackList = open("blackList.json","r",encoding="utf-8")
        blackList_read = blackList.read()
        new_blackList = json.loads(blackList_read)
        blackList_read.close()
        if guest_name not in blackList: # если введенное имя не присутствует в черном списке, то добавляем его в список гостей
            base_list = open("base.json","r",encoding="utf-8")
            base_list_read = base_list.read()
            new_base = json.loads(base_list_read) # из строки сделали массив
            new_base.append({
                    "guest_name" : guest_name
            }) # добавление введенного имени в список гостей
            base_list = json.dumps(base_list, ensure_ascii=False)
            base_list_write = open("base.json","w",encoding="utf-8")
            base_list_write.write(base_list)
            base_list_write.close()
        else: # в противном случай имя не добавляется
            print("Данный гость в черном списке!")
    else:
        print("Список гостей заполнен!")
guestAdd()

def guestDel():
    if len(base_list) > 0:
        guest_name = input("Введите имя: ")
        blackList = open("blackList.json","r",encoding="utf-8")
        blacklist_read = black_list.read()
        new_blackList = json.loads(blackList_read)
        new_blackList.append({
                "guest_name" : guest_name
        })
        blackList = json.dumps(blackList, ensure_ascii=False)
        blackList_write = open("blackList.json","w",encoding="utf-8")
        blackList_write.write(blackList)
        blackList_write.close()
        base_list = open("base.json","r",encoding="utf-8")
        base_list_read = base_list.read()
        new_base = json.loads(base_list_read) # из строки сделали массив
        new_base.remove(guest_name) # добавление введенного имени в список гостей
        base_list = json.dumps(base_list, ensure_ascii=False)
        base_list_write = open("base.json","w",encoding="utf-8")
        base_list_write.write(base_list)
        base_list_write.close()

        new_base.remove(guest_name) # удаление введенного имени из списка гостей если список не пуст
    else:
        print("Список пуст!")
guestDel()

def listShow():
    if len(base_list) > 0:
        textGuest = ""
        print("Список гостей: ")
        base_list = open("base.json","r",encoding="utf-8")
        base_list_read = base_list.read()
        new_base = json.loads(base_list_read) # из строки сделали массив
        base_list_read.close()
        for i in range(0,len(base_list)): #создаем цикл для просмотра списка гостей
            textGuest += f"{i + 1} - {guestList[i]}\n" # плюсуем к i единицу для того чтобы в выведенном списке отсчет начинался от 1, а не от 0
            print(textGuest) # вывод списка гостей если он не пуст
    else:
        print("Список пуст!")
listShow()