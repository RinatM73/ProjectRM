# цикл в цикле

# import time
# for h in range(0,24): # i = 1
#     for m in range(0,60): # j = 1
#         for s in range(0,60):
#             print(f"ч:{h} м:{m} с:{s}")
#             time.sleep(1)

# h = 0
# while h < 24:
#     m = 0
#     while m < 60:
#         s = 0
#         while s < 60:
#             print(f"{h}ч {m}м {s}с")
#             s = s + 1
#         m = m + 1
#     h = h + 1

# -------------------------------------------------------------------------------------------------------------------------------

# Использование циклов внутри циклов, возврат значений, + условия

print("Регистрация персонажа")
reg = 0
while reg < 1:
    reg_gender = 0
    while reg_gender < 1:
        gender = input("Выберите пол персонажа\n1-муж\n2-жен\n: ")
        if gender == "1":
            gender = "Мужской"
            reg_gender = 1
        elif gender == "2":
            gender = "Женский"
            reg_gender = 1
        else:
            print("Выберите из перечисленного")
        if reg_gender == 1:
            reg_race = 0
            while reg_race < 1:
                race = input(" 0-назад Выберите рассу персонажа\n1-Человек\n2-Эльф\n: ")
                if race == "1":
                    race = "Человек"
                    reg_race = 1
                elif race == "2":
                    race = "Эльф"
                    reg_race = 1
                elif race == "0":
                    reg_gender = 0
                    break
                else:
                    print("Ошибка: Выберите из перечисленного")
                if reg_race == 1:
                    reg_role = 0
                    if race == "Человек":
                        while reg_role == 0:
                            role = input("0-назад Выберите рассу персонажа\n1-Воин\n2-Лучник\n:")
                            if role == "1":
                                reg_role == 1
                    elif race == "Эльф":
    reg+=1
