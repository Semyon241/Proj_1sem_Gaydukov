# Вариант №4
import math

kilogramik = 0.0  # Присвоение переменной
a = (input('Введите цену конфет: '))
i = 0.0
while type(a) != float:  # Обработка исключений
    try:
        a = float(a)
        if a < 0:
            print('Введено неверное значение!')
            a = (input('Введите цену конфет заново: '))
    except ValueError:
        print('Введено неверное значение!')
        a = ('Введите вещественное число заново: ')
while kilogramik <= 0.9:  # Начало цикла
    kilogramik += 0.1
    i = a * kilogramik
    print(round(i, 2))  # Ответ
