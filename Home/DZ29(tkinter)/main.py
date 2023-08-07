from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("Кто вы по гороскопу?")
window.geometry('600x400+500+200')

def horoscope():
    if (combom['values'] == "Март" and combod['values'] >= 21) or (combom['values'] == "Апрель" and combod['values'] <= 20):
        sign = "Овен"
    elif (combom['values'] == "Апрель" and combod['values'] >= 21) or (combom['values'] == "Май" and combod['values'] <= 21):
        sign = "Телец"
    elif (combom['values'] == "Май" and combod['values'] >= 22) or (combom['values'] == "Июнь" and combod['values'] <= 21):
        sign = "Близнецы"
    elif (combom['values'] == "Июнь" and combod['values'] >= 22) or (combom['values'] == "Июль" and combod['values'] <= 22):
        sign = "Рак"
    elif (combom['values'] == "Июль" and combod['values'] >= 23) or (combom['values'] == "Август" and combod['values'] <= 21):
        sign = "Лев"
    elif (combom['values'] == "Август" and combod['values'] >= 22) or (combom['values'] == "Сентябрь" and combod['values'] <= 23):
        sign = "Дева"
    elif (combom['values'] == "Сентябрь" and combod['values'] >= 24) or (combom['values'] == "Октябрь" and combod['values'] <= 23):
        sign = "Весы"
    elif (combom['values'] == "Октябрь" and combod['values'] >= 24) or (combom['values'] == "Ноябрь" and combod['values'] <= 22):
        sign = "Скорпион"
    elif (combom['values'] == "Ноябрь" and combod['values'] >= 23) or (combom['values'] == "Декабрь" and combod['values'] <= 22):
        sign = "Стрелец"
    elif (combom['values'] == "Декабрь" and combod['values'] >= 23) or (combom['values'] == "Январь" and combod['values'] <= 20):
        sign = "Козерог"
    elif (combom['values'] == "Январь" and combod['values'] >= 21) or (combom['values'] == "Февраль" and combod['values'] <= 19):
        sign = "Водолей"
    elif (combom['values'] == "Февраль" and combod['values'] >= 20) or (combom['values'] == "Март" and combod['values'] <= 20):
        sign = "Лев"
    lbl4["text"] = (f'По гороскопу вы {sign}')
icon = PhotoImage(file = "stars1.png")
window.iconphoto(False, icon)
lbl = Label(window, text="Выберите свою дату рождения", font="Courier")
lbl.grid(column=0, row=0, columnspan=4, padx=130, pady=20)
lbl1 = Label(window, text="Число", font="Courier")
lbl1.grid(column=0, row=1)
lbl2 = Label(window, text="Месяц", font="Courier")
lbl2.grid(column=2, row=1)
lbl3 = Label(window, text="Год",font="Courier")
lbl3.grid(column=0, row=3, pady=20)
lbl4 = Label(window, font="Courier")
lbl4.grid(column=0, row=5)

combod = Combobox(window, width=3)
combod['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
combod.current(0) #Элемент выбранный по умолчанию
combod.grid(column=1, row=1)
combom = Combobox(window, width=10)
combom['values'] = ("Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь")
combom.current(0)
combom.grid(column=3, row=1)
txt = Entry(window,width=10)
txt.grid(column=1, row=3, pady=20)
btn = Button(window, command=horoscope, text="OK")
btn.grid(column=0, row=4, columnspan=4)
window.mainloop()