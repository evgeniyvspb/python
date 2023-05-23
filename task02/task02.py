# №2.2[11]. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является.
# Т.е. выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
# Примеры/Тесты:
# 5 -> в ряду Фибоначчи 5 имеет порядковый номер 6
# 6765 -> в в ряду Фибоначчи 6765 имеет порядковый номер 21
# 6766 -> -1
# Примечание: Вы можете решить эту задачу, используя формулу чисел Фибоначчи или итеративно.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711
# https://ru.wikipedia.org/wiki/Числа_Фибоначчи

num = int(input('enter nub]mber'))

first_num=0
second_num=1
third_num=first_num+second_num

count=3

while num>third_num:
    first_num=second_num
    second_num=third_num
    third_num=first_num+second_num
    count+=1

print(count) if third_num==num else print(-1)
