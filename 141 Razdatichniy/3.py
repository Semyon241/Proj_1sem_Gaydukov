#Вычисление суммы чисел с поддержкой вложенных списков

def summa(spis):
    if type(spis[0]) == list:
        spis[0] = sum(spis[0])
    if len(spis) == 1:
        return spis[0]
    return spis[0] + summa(spis[1:])

spisok = [1, [1, 2, 6], 7, 3]
result = summa(spisok)
print(result)