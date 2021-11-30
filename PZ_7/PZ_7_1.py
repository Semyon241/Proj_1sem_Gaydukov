# Дано целое число N (1 < N < 26). Вывести N первых прописных (то есть заглавных) букв латинского алфавита.
import random

N = random.randint(2, 25)
print('Ваше число: ', N, ' ')
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(s[:N])
