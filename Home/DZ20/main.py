def open():
    print("Входная дверь открыта")
def close():
    print("Входная дверь закрыта")
door = {
    "open" : open,
    "close" : close,
}

def on():
    print("Подогрев пола включен")
def off():
    print("Подогрев пола выключен")
floor = {
    "on" : on,
    "off" : off,
}

House = {
    "material" : "Кирпич",
    "windows" : {
        "profiles" : "Дерево",
        "colorW" : "Коричневый"
    },
    "color" : "Красный",
    "floor" : "Линолеум",
    "door" : {
        "materialD" : "Дерево",
        "colorD" : "Черный",
    },
    "levels" : "2",
    "rooms" : "6",
}

def showMaterial():
    print(f"Материал дома - {myHome['material']}")

def showWindowsProfiles():
    print(f"Материал окон - {myHome['windows']['profiles']}")

def showWindowsColor():
    print(f"Цвет окон - {myHome['windows']['colorW']}")

def showColor():
    print(f"Цвет дома - {myHome['color']}")

def showFloor():
    print(f"Материал пола - {myHome['floor']}")

def showDoorMaterial():
    print(f"Материал дверей - {myHome['door']['materialD']}")

def showDoorColor():
    print(f"Цвет дверей - {myHome['door']['colorD']}")

def showLevels():
    print(f"Количество этажей - {myHome['levels']}")

def showRooms():
    print(f"Количество комнат - {myHome['rooms']}")


myHome = House

showMaterial()
showWindowsProfiles()
showWindowsColor()
showColor()
showFloor()
showDoorMaterial()
showDoorColor()
showLevels()
showRooms()
myHome["floor"] = floor
myHome["door"] = door
myHome["door"]["open"]()
myHome["floor"]["off"]()