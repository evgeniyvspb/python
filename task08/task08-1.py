# 8.1[49]: Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. Доделать задание вебинара и реализовать Update, Delete
# Информация о человеке: Фамилия, Имя, Телефон, Описание

# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе
# (*) Усложнение.
# Сделать тесты для функций
# Разделить на model-view-controller

from os.path import join,abspath,dirname, exists

def Input_User()->list:
    user = list()
    user.append(input("Введите имя:       "))
    user.append(input("Введите фамилию:   "))
    user.append(input("Номер телефона:    "))
    user.append(input("Описание:          "))
    return user
 
def create (phone_dir_local: dict, idc: int, user: list)->dict:
    idc+=1
    phone_dir_local[idc]=user
    return phone_dir_local, idc
            
def export_phone_dir(phone_dir: dict):
    file_name=input("Введите имя файла, в который будут экспортированы данные:          ")
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name + ".txt")
    with open(full_name, mode = "w", encoding = "utf-8") as file:
        for idc, user in phone_dir.items():
            file.write(f"{idc}, {user[0]}, {user[1]}, {user[2]}, {user[3]}\n")

def import_phone_dir(phone_dir: dict):
    file_name=input("Введите имя файла, из которого будут импортированы данные:               ")
    MAIN_DIR = abspath(dirname(__file__))
    full_name = join(MAIN_DIR, file_name)
    if not exists(full_name):
        print("Ошибка программы! Такого файла я не смог найти....")
        return
    idc = len(phone_dir)+1
    with open(full_name, mode='r', encoding='utf-8') as file:
        for line in file:
            lst = line.strip().split(',')[1:]
            create(phone_dir, idc, lst)
            idc+=1
    return phone_dir, idc
 
def search_user(phone_dir:dict, searching: str) -> int:
    for idc, user in phone_dir.items():
        if user[0].startswith(searching):
            return idc
 
def print_dict(phone_dir:dict):
    for idc, user in phone_dir.items():    
        print(f"{idc}: {user[0]}, {user[1]}, {user[2]}, {user[3]}\n")
 
def reading(phone_dir:dict):
    searching = input("Кого в справочнике будем искать?   ")
    print(f"мы искали {phone_dir[search_user(phone_dir, searching)]}. Номер в справочнике {searching}")

def deleting(phone_dir:dict):
    print_dict(phone_dir)
    searching = int(input("Укажите номер позиции в справочнике, которую необхоимо удалить:   "))
    if searching in phone_dir:
        del phone_dir[searching]
    else: print("Такой позиции в списке нет. Извините и попробуйте еще раз")

def updating(phone_dir:dict):
    temping=list()
    print_dict(phone_dir)
    searching = int(input("Укажите номер позиции в справочнике, которую необхоимо изменить   "))
    if searching in phone_dir:
        del phone_dir[searching]
        print('Введите новые данные:    ')
        temping = Input_User()
        create(phone_dir, (searching-1), temping)
    else: print("Такой позиции в списке нет. Извините и попробуйте еще раз")

def menu():
    print('Меню справочника: 1- Create, 2 - Read, 3 - Update, 4 - Delete')
    print('                  5 - Export 6 - Import   7 - Print All')
    phone_dir = dict()
    key_count =0
    user=[]
    while True:    
        num = int(input("Введите желаемую операцию:   "))
        if num!=1 and num!=2 and num!=3 and num!=4 and num!=5 and num!=6 and num!=7:
            break
        if num==1:
            user = Input_User()
            phone_dir, key_count = create (phone_dir, key_count, user)
        if num==2:
            reading(phone_dir)
        if num==3:
            updating(phone_dir)
        if num==4:
            deleting(phone_dir)
        if num==5:
            export_phone_dir(phone_dir)
        if num==6:
            import_phone_dir(phone_dir)
        if num==7:
            print_dict(phone_dir)
        

menu() 
