from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Кто вы по гороскопу?")
window.geometry('600x400+500+200')

sign = ""

icon = PhotoImage(file = "stars1.png")

window.iconphoto(False, icon)

lbl = Label(window, text="Выберите свою дату рождения", font="Courier")
lbl.grid(column=0, row=0, columnspan=4, padx=130, pady=20)

lbl1 = Label(window, text="Число", font="Courier")
lbl1.grid(column=0, row=1, pady=70)

lbl2 = Label(window, text="Месяц", font="Courier")
lbl2.grid(column=2, row=1, pady=70)

combod = Combobox(window, width=3)
combod['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
day = combod['values']
combod.current(0) #Элемент выбранный по умолчанию
combod.grid(column=1, row=1)

combom = Combobox(window, width=10)
combom['values'] = ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
month = combom['values']
combom.current(0)
combom.grid(column=3, row=1)

def horoscope():
    global sign
    if (month == "Март" and day >= 21) or (month == "Апрель" and day <= 20):
        sign = "Овен"
    elif (month == "Апрель" and day >= 21) or (month == "Май" and day <= 21):
        sign = "Телец"
    elif (month == "Май" and day >= 22) or (month == "Июнь" and day <= 21):
        sign = "Близнецы"
    elif (month == "Июнь" and day >= 22) or (month == "Июль" and day <= 22):
        sign = "Рак"
    elif (month == "Июль" and day >= 23) or (month == "Август" and day <= 21):
        sign = "Лев"
    elif (month == "Август" and day >= 22) or (month == "Сентябрь" and day <= 23):
        sign = "Дева"
    elif (month == "Сентябрь" and day >= 24) or (month == "Октябрь" and day <= 23):
        sign = "Весы"
    elif (month == "Октябрь" and day >= 24) or (month == "Ноябрь" and day <= 22):
        sign = "Скорпион"
    elif (month == "Ноябрь" and day >= 23) or (month == "Декабрь" and day <= 22):
        sign = "Стрелец"
    elif (month == "Декабрь" and day >= 23) or (month == "Январь" and day <= 20):
        sign = "Козерог"
    elif (month == "Январь" and day >= 21) or (month == "Февраль" and day <= 19):
        sign = "Водолей"
    elif (month == "Февраль" and day >= 20) or (month == "Март" and day <= 20):
        sign = "Лев"
    lbl3 = Label(window,text=f'По гороскопу вы {sign}', font="Courier")
    lbl3.grid(column=0, row=5)
horoscope()

btn = Button(window, text="OK", command=horoscope)
btn.grid(column=0, row=4, columnspan=4, pady=70)

window.mainloop()