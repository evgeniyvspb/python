# #### 6.2[32]: Напишите функцию ```print_operation_table(operation, num_rows=6, num_columns=6)```, 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца, 
# т.е. функцию двух аргументов. Аргументы ```num_rows``` и ```num_columns``` указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.
	
# 	Примеры/Тесты:
#     print_operation_table(lambda x,y: x**y,4,4)
# 	1   1   1   1
# 	2   4   8  16
# 	3   9  27  81
# 	4  16  64 256

#     print_operation_table(lambda x,y: x*y)
# 	1   2   3   4   5   6
# 	2   4   6   8  10  12
# 	3   6   9  12  15  18
# 	4   8  12  16  20  24
# 	5  10  15  20  25  30
# 	6  12  18  24  30  36


# ```(*)``` **Усложнение.** Сформируйте форматированный вывод с номерами строк и столбцов
	
# 	Примеры/Тесты:
# 	print_operation_table(lambda x,y: x**y,4,4)
# 	       1   2   3   4
# 	    ----------------
# 	1 |    1   1   1   1
# 	2 |    2   4   8  16
# 	3 |    3   9  27  81
# 	4 |    4  16  64 256
	
# 	print_operation_table(lambda x,y: x*y)
# 	       1   2   3   4   5   6
# 	    ------------------------
# 	1 |    1   2   3   4   5   6
# 	2 |    2   4   6   8  10  12
# 	3 |    3   6   9  12  15  18
# 	4 |    4   8  12  16  20  24
# 	5 |    5  10  15  20  25  30
# 	6 |    6  12  18  24  30  36

def print_operation_table (operation, num_rows=6, num_columns=6):
    lengh1 = len(str(operation(num_rows, num_columns)))
    print('           ', end='')
    for idx in range(1,num_columns):
        print(f'{idx}',' '*(lengh1+2),end='')
    print(num_columns)
    print(f' '*5, '-'*(lengh1+4)*num_columns)
    for col1 in range(1,(num_rows+1)):
        print(f' {col1}  | ', end='')
        for rows1 in range(1,num_columns):
            # if col1*rows1<10: print(f' {operation(col1,rows1)}  ', end='')
            # else: print(f'  {operation(col1,rows1)} ', end='')
            print(f' '*(3+ lengh1 - len(str(operation(col1,rows1)))),operation(col1,rows1), end ='')
        print(f' '*(3+ lengh1 - len(str(operation(col1,num_columns)))),operation(col1,num_columns))
        # print(f'  {operation(col1,num_columns)}')

print_operation_table(lambda x,y: x**y,4,4)
print_operation_table(lambda x,y: x*y)