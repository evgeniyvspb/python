"""
№1.1[1]. За день машина проезжает n километров.
Сколько дней нужно, чтобы проехать маршрут длиной m километров?
Реализуйте пользовательский ввод данных и вывод внятного результата. Используйте .format() или f-строки
Примеры/Тесты:
n = 700, m = 750 -> Чтобы проехать 750км машине потребуется 2дн
n = 700, m = 600 -> Чтобы проехать 600км машине потребуется 1дн
n = 700, m = 1400 -> Чтобы проехать 1400км машине потребуется 2дн
Усложнение[*]. Использовать тернарный оператор
"""
n = int(input('сколько проезжает за день'))
m= int(input('сколько надо проехать киллометров'))
day = -(-m//n)
print(f'чтобы проехать {m} киллометров потребуется {day}')
