# Вариант №4: 2)	Описать функцию RectPS(x1,y1,x2,y2,P,S), вычисляющую периметр Р и площадь S прямоугольника со сторонами, параллельными осям координат, по координатам (х1, у1), (х2, у2) его противоположных вершин (х1, у1, х2, у2 – входные, Р и S – выходные параметры вещественного типа).
# С помощью этой функции найти периметры и площади трех прямоугольников с данными  противоположными вершинами.
def rectps(x1, y1, x2, y2):  # Определение функции
    p = 2 * ((x2 - x1) + (y2 - y1))
    s = (x2 - x1) * (y2 - y1)
    return p, s
for i in range(3):
    a1 = int(input('Введите a1: '))
    b1 = int(input('Введите b1: '))
    a2 = int(input('Введите a2: '))
    b2 = int(input('Введите b2: '))
    print('Периметр прямоугольника: {}. Площадь прямоугольника: {}'.format(*rectps(a1, b1, a2, b2))) #Вывод результата