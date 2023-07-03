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
    "material" : "",
    "windows" : {
        "profiles" : "",
        "colorW" : ""
    },
    "color" : "",
    "floor" : "",
    "door" : {
        "materialD" : "",
        "colorD" : "",
    },
    "levels" : "",
    "rooms" : "",
}

myHome = House
myHome["material"] = "Кирпич"
myHome["windows"]["profiles"] = "Дерево"
myHome["windows"]["colorW"] = "Коричневый"
myHome["color"] = "Красный"
myHome["floor"] = "Линолеум"
myHome["floor"] = floor
myHome["door"]["materialD"] = "Дерево"
myHome["door"]["colorD"] = "Черный"
myHome["door"] = door
myHome["levels"] = "2 этажа"
myHome["rooms"] = "6 комнат"
print(myHome)
myHome["door"]["open"]()
myHome["floor"]["off"]()