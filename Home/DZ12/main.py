print("Регистрация персонажа")
reg = 0
while reg == 0:
    reg_gender = 0
    while reg_gender == 0:
        gender = input("Выберете пол персонажа\n1 - М\n2 - Ж\n>  ")
        if gender == "1":
            gender = "Мужской"
            reg_gender=1
        elif gender == "2":
            gender = "Женский"
            reg_gender=1
        else:
            print("Ошибка: Выберите из перечисленного")
        if reg_gender == 1:
            reg_race = 0
            while reg_race == 0:
                race = input("Выберете рассу пресонажа\n1 - Человек\n2 - Эльф\n3 - Гном\n4 - Назад\n5 - К началу\n>  ")
                if race == "1":
                    race = "Человек"
                    reg_race = 1
                elif race == "2":
                    race = "Эльф"
                    reg_race = 1
                elif race == "3":
                    race = "Гном"
                    reg_race = 1
                elif race == "4":
                    reg_gender = 0
                    break
                elif race == "5":
                    reg_gender = 0
                    break
                else:
                    print("Ошибка: Выберете из перечисленного")
                if reg_race == 1:
                    reg_role = 0
                    if race == "Человек":
                        while reg_role == 0:
                            role = input("Выберете роль пресонажа\n1 - Мечник\n2 - Лучник\n3 - Кавалерист\n4 - Назад\n5 - К началу\n>  ")
                            if role == "1":
                                role = "Мечник"
                                reg_role = 1
                            elif role == "2":
                                role = "Лучник"
                                reg_role = 1
                            elif role == "3":
                                role = "Кавалерист"
                                reg_role = 1
                            elif role == "4":
                                reg_race = 0
                                break
                            elif role == "5":
                                reg_gender = 0
                                break
                            else:
                                print("Ошибка: Выберете из перечисленного")
                            if reg_role == 1:
                                reg_name = 0
                                while reg_name == 0:
                                    myName = input("Введите имя: ")
                                    info = input("Вывести информацию о персонаже?\n1 - Да\n2 - Нет\n>  ")
                                    if info == "1":
                                        print("Информация о персонаже: ")
                                        print("Имя: ",myName)
                                        print("Пол: ",gender)
                                        print("Раса: ",race)
                                        print("Роль: ",role)
                                    elif info == "2":
                                        reg_gender = 0
                                    else:
                                        print("Ошибка: Выберите из перечисленного")
                    elif race == "Эльф":
                        while reg_role == 0:
                            role = input("Выберете роль пресонажа\n1 - Мечник\n2 - Лучник\n3 - Кавалерист\n4 - Назад\n5 - К началу\n>  ")
                            if role == "1":
                                role = "Мечник"
                                reg_role = 1
                            elif role == "2":
                                role = "Лучник"
                                reg_role = 1
                            elif role == "3":
                                role = "Кавалерист"
                                reg_role = 1
                            elif role == "4":
                                reg_race = 0
                                break
                            elif role == "5":
                                reg_gender = 0
                                break
                            else:
                                print("Ошибка: Выберете из перечисленного")
                            if reg_role == 1:
                                reg_name = 0
                                break
                    elif race == "Гном":
                        while reg_role == 0:
                            role = input("Выберете роль пресонажа\n1 - Мечник\n2 - Копейщик\n3 - Арбалетчик\n4 - Назад\n5 - К началу\n>  ")
                            if role == "1":
                                role = "Мечник"
                                reg_role = 1
                            elif role == "2":
                                role = "Копейщик"
                                reg_role = 1
                            elif role == "3":
                                role = "Арбалетчик"
                                reg_role = 1
                            elif role == "4":
                                reg_race = 0
                                break
                            elif role == "5":
                                reg_gender = 0
                                break
                            else:
                                print("Ошибка: Выберете из перечисленного")
                            if reg_role == 1:
                                reg_name = 0
                                break
                        pass
 
    reg+=1
