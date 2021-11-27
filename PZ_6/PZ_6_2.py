# Дан список размера N. Найти номер его поседнего локального максимума.

import random

spisok = [random.randint(-100, 100) for _ in range(6)]
maxi = []
for i in range(len(spisok) - 1):  # Вызов оператора for
    if spisok[i] > spisok[i - 1]:
        if spisok[i] > spisok[i + 1]:
            maxi.append(spisok[i])
print(spisok)
print(maxi)
print(spisok.index(maxi[-1]))
