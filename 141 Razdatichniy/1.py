# Вычислить сумму элементов набора чисел

def summa(spis):
    if len(spis) == 1:
        return spis[0]
    return spis[0] + summa(spis[1:])


print(summa([2, 4, 6, 8, 10, 12]))
