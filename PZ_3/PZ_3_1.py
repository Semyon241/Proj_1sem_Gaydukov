import math
A=input('Введите целое число: ')#Ввод исходных значений
while type(A) !=int:#Обработка исключений
    try: A =int(A)
    except ValueError :
        print('Введено некоректное значение!')
        A=input('Введите целое число заново: ')
B=input('Введите второе целое число: ')#Ввод исходных значений
while type(B) !=int:#Обработка исключений
    try: B=int(B)
    except ValueError :
        print('Введено некорректное значение')
        B=input('Введите второе целое число заново: ')
if (A>2 & B<3):
 print('Неравенства справедливы!')#Ответ
else:
 print('Неравенства несправедливы.')#Ответ