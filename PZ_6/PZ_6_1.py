# Вариант 4: Дан первый член А и знаменатель D геометричесой прогрессии.
# Сформировать и вывести список размера 10, содержащий 10 первых членов прогрессии:
# A, A * D, A * D ** 2, A * D ** 3, ...

import random

A = random.randint(2, 12)
D = random.randint(2, 12)
my_list = []
for i in range(10):  # Вызов оператора for
    my_list.append(A * D ** i)
print(A, D, my_list, sep='\n')  # Ответ
