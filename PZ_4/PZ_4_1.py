import math

i = float(input('Введите цену 1 кг конфет: '))
while type(i) != float:
    try:
        i = float(i)
        if i < 0:
            print('Вы ввели неправильное значение!')
            i = float(input('Введите цену 1 кг конфет заново: '))
    except ValueError:
        print('Введено неверное значение!')
        i = float(input('Введите цену 1 кг конфет:  '))
