# Вычислить количество отрицательных чисел в наборе

def vi(spisok):
    if spisok[0] < 0:
        if len(spisok) == 1:
            return 1
        return 1 + vi(spisok[1:])
    return 0 + vi(spisok[1:])


my_list = [11, 42, -32, -41, -15]
result = vi(my_list)
print(result)
