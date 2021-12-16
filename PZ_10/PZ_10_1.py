# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Минимальный элемент:
# Элементы, умноженные на первый максимальный элемент:

from random import randint

my_list = list(str(randint(-100, 100)) for i in range(randint(10, 20)))
print(my_list)

with open('file.txt', 'w+', encoding='utf-8') as init_file:
    init_file. writelines(' '.join(my_list))

with open('file.txt', 'r', encoding='utf-8') as init_file:
    init_list = list(init_file.read().split(' '))
    print(init_list)
    with open('main_file.txt', 'w+', encoding='utf-8') as main:
        main.writelines(f"Исходные данные: \n{' '.join(init_list)}\n\n"
                        f"Количество эдементов: \n{len(init_list)}\n\n"
                        f"Минимальный элемент: \n{min([int(i) for i in init_list])}\n\n"
                        f"Все элементы, умноженные на максимальный из них:\n"
                        f"{[(int(i) * int(max([int(i) for i in init_list]))) for i in init_list]}")
