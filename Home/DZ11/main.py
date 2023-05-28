# Задание 1

# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
# for i in range(start,end + 1):
#     if i % 7 == 0:
#         print(i)

# Задание 2

# start = int(input("Введите начало диапазона: "))
# end = int(input("Введите конец диапазона: "))
# print("Все числа диапазона")
# for i in range(start,end + 1):
#     print(i)
# print("В обратном порядке")
# for i in range(start - 1,end):
#     print(end)
#     end = end - 1
# print("Все числа кратные 7")
# for i in range(start,end + 1):
#     if i % 7 == 0:
#         print(i)
# print("Количество чисел кратных 5")
# n = 1
# for i in range(start,end + 1):
#     if i % 5 == 0:
#         print(n)
#         n = n + 1

# Задание 3

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
while start < end:
    start = start + 1
    if start % 3 == 0 and start % 5 != 0:
        print("Fizz")
    elif start % 5 == 0 and start % 3 != 0:
        print("Buzz")
    elif start % 3 == 0 and start % 5 == 0:
        print("Fizz Buzz")
    elif start % 3 != 0 and start % 5 != 0:
        print(start)
