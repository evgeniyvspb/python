# 	Примеры/Тесты:
# 		<function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", False) -> True
# 	    <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам", True) -> (True, [{'а': 4}, {'а': 4}, {'а': 4}])
# 	    <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> (True, [{'а': 4}, {'а': 2, 'у': 2}, {'а': 2, 'е': 1, 'о': 1}])
# 	    <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> (False, [{'а': 4}, {'а': 2, 'у': 3}])
# 	    <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> (False, [{'а': 11}, {'у': 6, 'а': 3}])
# 	    <function_name>("Пам-парам-пурум Пум-пурум-карам") -> (True, [{'а': 3, 'у': 2}, {'у': 3, 'а': 2}])

def search_glas(str1:str, param=True) -> str:
    glasnie_bukvi =  ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
    count_rez = 0
    rez_str = str1.split()
    glassnih=0
    search_glas = 'True'
    for item in range(len(rez_str[0])):
        if glasnie_bukvi.count(rez_str[0][item]) !=0: glassnih+=1
    for idx in range(1,len(rez_str)):
        for item in range(len(rez_str[idx])):
            if glasnie_bukvi.count(rez_str[idx][item]) !=0: count_rez+=1
        if glassnih != count_rez: search_glas = 'False'
        count_rez=0
    if param !=False:
        glassnih={}
        glassnih_final=[]
        for pesnya in range(len(rez_str)):
            for idx in range(len(glasnie_bukvi)):
                if rez_str[pesnya].count(glasnie_bukvi[idx]) !=0 : 
                    glassnih[glasnie_bukvi[idx]]= rez_str[pesnya].count(glasnie_bukvi[idx])
            glassnih_final.append(str(glassnih))  # Я НЕ СМОГ ПОНЯТЬ!!! как убрать привязку glassnih и glassnih_final (придумал разве что конверт в строку), 
                                    # при очищении словаря автоматом очищается и список :=((( если есть идеи, буду благодарен   
            glassnih.clear()
        return (f'{search_glas} {glassnih_final}')
    else: return search_glas
                
        
print(search_glas("пара-ра-рам рам-пам-папам па-ра-па-дам", False))        
print(search_glas("пара-ра-рам рам-пам-папам па-ра-па-дам", True))
print(search_glas("пара-ра-рам рам-пум-пупам па-ре-по-дам"))
print(search_glas("пара-ра-рам рам-пуум-пупам па-ре-по-дам"))
# я посчитал алогичгым выводить при False количесетво букв только в  двух. ведь по логике надо бы всё показать раз указан парметр показать количество букв
print(search_glas("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па"))
print(search_glas("Пам-парам-пурум Пум-пурум-карам"))     
