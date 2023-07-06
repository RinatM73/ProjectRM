class Korpus:
    def __init__(self, blockpit, matplata, proc, operpam, vidcard, postpam):
        self.blockpit = blockpit
        self.matplata = matplata
        self.proc = proc
        self.operpam = operpam
        self.vidcard = vidcard
        self.postpam = postpam

class BlockPit:
    def __init__(self, form, power):
        self.form = form
        self.power = power

    def start(self):
        print("Запуск блока питания")

    def stop(self):
        print("Стоп")

class MatPlata:
    def __init__(self, tip, marka):
        self.tip = tip
        self.marka = marka

    def start(self):
        print("Запуск материнской платы")

    def stop(self):
        print("Стоп")

class Proc:
    def __init__(self, yadro, chast):
        self.yadro = yadro
        self.chast = chast

    def start(self):
        print("Запуск процессора")

    def stop(self):
        print("Стоп") 

class Operpam:
    def __init__(self, pamyat, marka):
        self.pamyat = pamyat
        self.marka = marka

    def start(self):
        print("Запуск процессора")

    def stop(self):
        print("Стоп")

class Vidcard:
    def __init__(self, pamyat, marka)

    def start(self):
        print("Запуск видеокарты")

    def stop(self):
        print("Стоп")