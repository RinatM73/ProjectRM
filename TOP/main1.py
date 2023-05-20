# a = 5
# b = 10
# if a > b: 
#     print("if выполнился")
# elif a < b:
#     print("elif выполнился")    
# else:
#     print("else выполнился")

# login = input("Введите логин : ")
# password = input("Введите пароль : ")
# if login == "admin":
#     if password == "admin":
#         print("Вход выполнен")
#     else:
#         print("Неверный логин или пароль : 2 этап")
# else:
#     print("Неверный логин или пароль : 1 этап")

# q1 = input("Зимой и летом одним цветом : ")
# score = 0
# if q1 == "ёлка" or q1 == "елка":
#     print("Ответ верный")
#     score = score + 1
# else:
#     print("Ответ неверный")

# q2 = input("Какое сегодня число? : ")
# if q2 == "19":
#     print("Ответ верный")
#     score = score + 1
# else:
#     print("Ответ неверный")

# q3 = input("Кто его раздевает тот слезы раздевает : ")
# if q3 == "лук":
#     print("Ответ верный")
#     score = score + 1
# else:
#     print("Ответ неверный")

# q4 = input("Два кольца два конца, посередине гвоздик : ")
# if q4 == "ножницы":
#     print("Ответ верный")
#     score = score + 1
# else:
#     print("Ответ неверный")

# q5 = input("Сколько будет 3 в кубе?  ")
# if q5 == "27":
#     print("Ответ верный")
#     score = score + 1
    
# else:
#     print("Ответ неверный")


# if score > 3:
#     q6 = input("Ответите на бонусный вопрос?")
#     if q6 == "да":
#         q7 = input("Я готов к учебным стартам, скоро сяду я за...? ")
#         if q7 == "парту":
#             print("Ответ верный")
#             score = + 1
#         else:
#             print("Ответ неверный")
#     else:
#         print("Всего доброго!")
# else:
#     print("Спасибо за игру!")

# x = 5
# if x % 2 == 0:
#     print("четное")
# else:
#     print("нечетное")


x1 = int(input("Введите число 1 : "))
x2 = int(input("Введите число 2 : "))

y = input("Выберите действие (сложение 1, разница 2, ср. арифм 3, произведение 4): ")
if y == "1":
    print(x1 + x2)
elif y == "2":
    print(x1 - x2)
elif y == "3":
    print((x1 + x2) / 2)
elif y == "4":
    print(x1 * x2)
else:
    print("До свидания!")

     

