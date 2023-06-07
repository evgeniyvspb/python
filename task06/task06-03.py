# # №6.3[43] Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу, образуют одну пару, которую необходимо посчитать.
# Напишите функцию
# Аргументы: список целых чисел
# Возвращает: кол-во пар
# Примеры/Тесты:
# <function_name>([1, 2, 3, 2, 3]) -> 2
# <function_name>([1, 2, 3, 2, 3, 3, 2, 4]) -> 6

# def co_p(lis1:list):
#     result=0
#     for idx in range(len(lis1)):
#         for idx2 in range(idx+1,len(lis1)):
#             if lis1[idx]==lis1[idx2]: result+=1
#     return result
    
def co_p(lis1:list):
    result=0
    for idx in range(len(lis1)):
        result += lis1[idx+1:].count(lis1[idx])  # срез нужен чтобы пробегать только дальше а не с начала
    return result

print(co_p([1, 2, 3, 2, 3]))