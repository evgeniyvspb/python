"""
#### 1.4[8]. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
	Примеры/Тесты:
	3 2 4 -> yes
	3 2 1 -> no
"""
print('enter size of chocolate')
n = int(input('n =  '))
m = int(input('m =  '))
k= int(input('how much pieces need to cut'))
print('yes') if k%n==0 or k%m==0 else print('no')

