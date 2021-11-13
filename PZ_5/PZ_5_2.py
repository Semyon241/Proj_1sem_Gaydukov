def rectps(x1, y1, x2, y2):
    p = 2 * ((x2 - x1) + (y2 - y1))
    s = (x2 - x1) * (y2 - y1)
    return p, s
for i in range(3):
    a1 = int(input('Введите a1: '))
    b1 = int(input('Введите b1: '))
    a2 = int(input('Введите a2: '))
    b2 = int(input('Введите b2: '))
    print('Периметр прямоугольника: {}. Площадь прямоугольника: {}'.format(*rectps(a1, b1, a2, b2)))