# Задача 3

# x = int(input("Введите число месяца (от 1 до 12): "))
# if x == (1 or 2 or 12):
#     print("Zima")
# elif x == (3 or 4 or 5):
#     print("Vesna")
# elif x == (6 or 7 or 8):
#     print("Osen'")
# elif x == (9 or 10 or 11):
#     print("Zima")
# else:
#     print("Oshibka")

# Проверка високосного года

# x = int(input("Введите год: "))
# if x % 4 != 0:
#     print("Год обычный")
# elif x % 4 == 0:
#     if x % 100 != 0:
#         print("Год високосный")
#     elif x % 100 == 0:
#         if x % 400 == 0:
#             print("Год високосный")
#         else:
#             print("Год обычный")
#     else:
#         print()
# else:
#     print()

# Проверка треугольника

# x = int(input("Введите сторону 1: "))
# y = int(input("Введите сторону 2: "))
# z = int(input("Введите сторону 3: "))
# if x + y > z or x + z > y or y + z > x:
#     print("Треугольник существует")
#     if x != y and x != z and y != z:
#         print("Треугольник разносторонний")
#     elif x == y == z:
#         print("Треугольник равносторонний")
#     else:
#         print("Треугольник равнобедренный")
# else:
#     print("Трегольник не существует")

# Персонаж

nameGame = "Подземелья"
print("Добро пожаловать \n 'Подземелья'")

print("Выберите пол персонажа:\n", "ж-женский\n", "м-Мужской")
gender = str(input("Введите ж или м :\n"))
if gender == "М" or gender == "м":
  gender = "Мужской"
elif gender == "Ж" or gender == "ж":
  gender = "Женский"
print(f"Вы выбрали {gender} пол")

print("Выберете расу персонажа ч-человек,\n э-эльф")
race = str(input("Введите ч или э:\n"))
if race == "ч" or race == "Ч":
  race = "Человек"
elif race == "э" or race == "Э":
  race = "Эльф"
 
  print(f"Вы выбрали рассу {race}")

if race == "Человек":
  scoreRole = 0  # галочка для выбора класса
  print("Выберете класс:\n", "1-Воин", "2-Лучник", "3-Жрец", "4-Маг")
  role = input("введите 1,2,3 или 4 для выбора класса:")
  if role == "1":
    role = "Воин\n"
  elif role == "2":
    role = "Лучник\n"
  elif role == "3":
    role = "Жрец\n"
  elif role == "4":
    role = "Маг\n"

elif race == "Эльф":
    print("Выберете класс:\n", "1-Воин\n", "2-Лучник\n", "3-Темный Колдун\n",
          "4-Паладин\n")
    role = input("введите 1,2,3 или 4 для выбора класса")
    if role == "1":
      role = "Воин"
    elif role == "2":
      role = "Лучник"
    elif role == "3":
      role = "Темный Колдун"
    elif role == "4":
      role = "Паладин"
print(f"Вы выбрали класс:{role}")

name = str(input("Введите имя вашего персонажа"))
print("\nИнформация о персонаже:\n"
        f"пол персонажа {gender}\n"
        f"Раса персонажа {race}\n"
        f"Класс:{role}\n"
        f"Имя:{name}\n")