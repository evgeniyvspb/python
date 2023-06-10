    # №7.1[###]. Дан текстовый csv файл. Разделитель данных #.
# Каждая строка файла представляет собой запись вида ФИО
# Например:
# Иванов#Иван#Иванович
# Петров#Петр#Петрович
# Соколов#Илья#Григорьевич
# 1) Необходимо вывести эти данные на экран построчно в виде:
# Иванов Иван Иванович
# Петров Петр Петрович
# 2) записать эти данные в список вида: [['Иванов', 'Иван', 'Иванович'], ['Петров', 'Петр', 'Петрович']...]
# [*] Усложнение. Файл находится в поддиретории data текущей директории. Сформировать путь к нему с использованием
# # os.path и pathlib
# необходимо преобразовать к виду:
# Иванов И.И.
# Петров П.П.
# Полученные строки записать в новый файл. Файл должен находиться в поддиретории rezults.
# [*] Усложнение. Данные необходимо записать в два разных файла:
# В первый - в виде Иванов И.И.
# Во второй - в виде Иванов-И-И
# [*****] Усложнение. Вам известно, что (в перспективе) подобных спецификаций может быть много. Не две, а пять или десять
# Как улучшить свой код в этом случае, сделать его легко расширяемым?

import os
print (os.getcwd())
import os.path as path1
 
MAIN_DIR = path1.abspath(path1.dirname(__file__))
file_name = path1.join(MAIN_DIR, "data1.txt")
# print(file_name)
 
with open (file_name, "r", encoding="utf-8") as data:
    result_list = list()
    for item in data:
        last_name, first_name, parent = item.strip().split("#")
        print (last_name, first_name, parent)
        list1={last_name, first_name, parent}
        result_list.append(list1)
    print(result_list)


for last_name, first_lit, parent in result_list:
    str1 = f"{last_name} {first_lit[0]}.{parent[0]}."
    print (str1)

file_name2 = path1.join(MAIN_DIR, 'results',"names.txt") 
with open(file_name2, 'wt',encoding="utf-8") as result_file:
    for last_name, first_lit, parent in result_list:
        str1 = f"{last_name} {first_lit[0]}.{parent[0]}.\n" #чтобы пернести на след строку
        result_file.write(str1)

