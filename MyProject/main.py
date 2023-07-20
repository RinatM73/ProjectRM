from classes.Manager import * #звездочка выбирает все файлы из папки classes, можно перечислить файлы через запятую
import json

def reg():
    store_list_read = open("./store/store.json","r",encoding="utf-8") # читаем файл
    store_list = json.loads(store_list_read.read()) # из строки делаем массив
    store_list_read.close()
    print(store_list)
    regs = Registration()
    regs.create_user(store_list)
    store_list = json.dumps(store_list, ensure_ascii=False)
    store_list_write = open("./store/store.json","w",encoding="utf-8")
    store_list_write.write(store_list)
    store_list_write.close()
reg()