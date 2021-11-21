# Вариант №4: Дано целое число N (> 0).
# Используя операции деления нацело и взятия остатка от деления, найти число, полученное при прочтении числа N справа налево.
import math

N = input('Введите целое число: ')  # Ввод переменной
while type(N) != int:  # Обработка исключений
    try:
        N = int(N)
        if N < 0:
            print('Введено неправильное значение!')
            N = input('Введите целое число заново: ')
    except ValueError:
        print('Введено неправильное значение!')
        N = input('Введите целое число заново: ')
T = input('Введите целое число на которое будет делиться N: ')
while type(T) != int:  # Обработка исключений
    try:
        T = int(T)
        if T < 0:
            print('Введено неправильное значение!')
            T = input('Введите целое число заново: ')
    except ValueError:
        print('Введено неправильное значение!')
        T = input('Введите целое число заново: ')
print('При целочисленном делении N на T получится:', N // T)
print('При взятии остатка от деления N на T мы получим:', N % T)
print(f'{N % T}.{N // T}'' - число, полученное при прочтении числа N справа налево.')  # Ответ
