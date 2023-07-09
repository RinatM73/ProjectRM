class Korpus:
    def __init__(self, blockpit, matplata, proc, operpam, vidcard, postpam):
        self.blockpit = blockpit
        self.matplata = matplata
        self.proc = proc
        self.operpam = operpam
        self.vidcard = vidcard
        self.postpam = postpam
    
    def start(self):
        print("ПК загружен")

    def stop(self):
        print("ПК выключен")


class BlockPit:
    def __init__(self, marka, form, power):
        self.marka = marka
        self.form = form
        self.power = power

    def start(self):
        print("Запуск блока питания")

    def stop(self):
        print("Стоп")

    def showBlockpit(self):
        print("")



class MatPlata:
    def __init__(self, marka, form, chipset):
        self.marka = marka
        self.form = form
        self.chipset = chipset

    def start(self):
        print("Запуск материнской платы")

    def stop(self):
        print("Стоп")

class Proc:
    def __init__(self, marka, cores, freq):
        self.marka = marka
        self.cores = cores
        self.freq = freq

    def start(self):
        print("Запуск процессора")

    def stop(self):
        print("Стоп") 

class Operpam:
    def __init__(self, marka, standart, ram):
        self.marka = marka
        self.standart = standart
        self.ram = ram

    def start(self):
        print("Запуск оперативной памяти")

    def stop(self):
        print("Стоп")

class Vidcard:
    def __init__(self, marka, vram, clockspeed):
        self.marka = marka
        self.vram = vram
        self.clockspeed = clockspeed


    def start(self):
        print("Запуск видеокарты")

    def stop(self):
        print("Стоп")

class Postpam:
    def __init__(self, marka, vid, memory):
        self.marka = marka
        self.vid = vid
        self.memory = memory

    def start(self):
        print("Запуск постоянной памяти")

    def stop(self):
        print("Стоп")

myBlockPit = BlockPit("Aerocool","ATX",750)
myMatPlata = MatPlata("ASUS","ATX","AMD B450")
myProc = Proc("Intel Core i5",4,2.5)
myOperpam = Operpam("Samsung","DDR4",8)
myVidcard = Vidcard("Nvidia GeForce GTX1050i",4,7000)
myPostpam = Postpam("Samsung","SSD",256)
myPC = Korpus(myBlockPit,myMatPlata,myProc,myOperpam,myVidcard,myPostpam)


def globalReg():
    vybor = int(input("Выберите действие:\n1 - Включить ПК\n2 - Выключить ПК\n3 - Показать информацию о ПК\n>"))
    if vybor == 1:
        myPC.blockpit.start()
        myPC.matplata.start()
        myPC.proc.start()
        myPC.operpam.start()
        myPC.vidcard.start()
        myPC.postpam.start()
        myPC.start()

    elif vybor == 2:
        myPC.blockpit.stop()
        myPC.matplata.stop()
        myPC.proc.stop()
        myPC.operpam.stop()
        myPC.vidcard.stop()
        myPC.postpam.stop()
        myPC.stop()

    elif vybor == 3:
        print(f"Блок питания:\nМарка: {myBlockPit.marka}\nФорм-фактор: {myBlockPit.form}\nМощность: {myBlockPit.power} Вт\n")
        print(f"Материнская плата:\nМарка: {myMatPlata.marka}\nФорм-фактор: {myMatPlata.form}\nЧипсет: {myMatPlata.chipset}\n")
        print(f"Процессор:\nМарка: {myProc.marka}\nКоличество ядер: {myProc.cores}\nЧастота: {myProc.freq} Ггц\n")
        print(f"Оперативная память:\nМарка: {myOperpam.marka}\nСтандарт: {myOperpam.standart}\nRAM: {myOperpam.ram} Гб\n")
        print(f"Видеокарта:\nМарка: {myVidcard.marka}\nVRAM: {myVidcard.vram} Гб\nЧастота: {myVidcard.clockspeed} Мгц\n")
        print(f"Постоянная память:\nМарка: {myPostpam.marka}\nТип: {myPostpam.vid}\nОбъем: {myPostpam.memory} Гб\n")
globalReg()