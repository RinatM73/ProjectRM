numberList = [5, 16, 7, 24, 3]
numberList1 = [11, 3, 52, 5, 13]
print("Все элементы списков")
numberList2 = numberList + numberList1
print(numberList2)
print("------------------------------------")
print("Все элементы списков без повторений")
print(set(numberList2))
print("------------------------------------")
print("Общие элементы списков")
numberList3 = []
for i in numberList:
    for j in numberList1:
        if i == j:
            numberList3.append(i)
            break
print(numberList3)
print("------------------------------------")
print("Уникальные элементы списков")
numberList4 = []
for i in numberList1:
    if i not in numberList:
        numberList4.append(i)
for i in numberList:
    if i not in numberList1:
        numberList4.append(i)
print(numberList4)
print("------------------------------------")
print("Максимальные и минимальные элементы обоих списков")
numberList5 = [max(numberList), min(numberList), max(numberList1), min(numberList1)]
print(numberList5)
print("------------------------------------")