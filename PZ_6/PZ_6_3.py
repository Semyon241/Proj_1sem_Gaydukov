# Дан список размера N. Переставить в обратном порядке элементы списка,
# расположенные между его минимальным и максимальным элементами, включая
# минимальный и максимальный элементы.
import random
my_list = [random.randint(0, 100) for i in range(6)]
print(my_list)
els = sorted([my_list.index(max(my_list)), my_list.index(min(my_list))])
my_list = my_list[:els[0]] + [i for i in reversed(my_list[els[0]:els[1] + 1])] + my_list[els[1]+1:]
print(my_list)
