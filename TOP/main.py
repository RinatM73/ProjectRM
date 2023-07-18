# base_list - база данных как SQL, не может хранить классы, функции и методы, она храниться где-то на сервере

# base_list = [
#     {
#         "first_name" : "Денис",
#         "last_name" : "Кириллов",
#         "birthday" : "01.06.2001",
#         "gender" : "Мужской",
#         "login" : "denis161",
#         "password" : "12345"
#     },
#     {
#         "first_name" : "Кирилл",
#         "last_name" : "Кириллов",
#         "birthday" : "17.08.2006",
#         "gender" : "Мужской",
#         "login" : "kirillooo",
#         "password" : "12345"
#     },
#     {
#         "first_name" : "Максим",
#         "last_name" : "Максимов",
#         "birthday" : "11.04.2000",
#         "gender" : "Мужской",
#         "login" : "maks07",
#         "password" : "12345"
#     },
#     {
#         "first_name" : "Руслан",
#         "last_name" : "Русланов",
#         "birthday" : "11.02.2000",
#         "gender" : "Мужской",
#         "login" : "russlan",
#         "password" : "12345"
#     },
#     {
#         "first_name" : "Екатерина",
#         "last_name" : "Исаева",
#         "birthday" : "25.10.2000",
#         "gender" : "Женский",
#         "login" : "ekaterina25e",
#         "password" : "12345"
#     },
# ]
# registered_users = [    # обработанная база данных с сервера, хранит в себе весь функционал пользователей, модераторов и админа.

# ]

# # r - только чтение файла  read()
# # w - запись write()
# # a - добавить в конец файла текст write()
# # + - чтение и запись
# fileW = open("text.txt","w",encoding="utf-8")
# # print(file.read(5)) # показывает первые пять символов
# fileW.write("Новый текст\n")
# fileW.write("Новый текст")
# fileW.close()

# fileR = open("text.txt","r",encoding="utf-8")
# print(fileR.read())
# fileR.close()

import json
# открыли файл с возможностью чтения
base_list = open("base.json","r",encoding="utf-8")
# открыли файл на чтение
base_list_read = base_list.read()
new_base = json.load(base_list_read) # 
new_base.append({
        "first_name" : "Собака",
        "last_name" : "",
        "birthday" : "17.08.2006",
        "gender" : "Мужской",
        "login" : "dog",
        "password" : "12345"
})
print(new_base[5])
dumps_base = json.dumps(new_base) # из массива сделали строку
file = open("base.json","w",encoding="utf-8")
file.write



# primer = '[{"first_name" : "Denis", "age" : 22},{"first_name" : "Masha", "age" : 18}]'
# print(primer)
# massiv = json.loads(primer)
# print(massiv[0]) # информация о нулевом объекте массива



