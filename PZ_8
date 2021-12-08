# Дан словарь с четным количеством элементов. Найти суммы значений
# элементов первой и второй половин с использованием функции. Результаты вывести
# на экран.

nums2 = {'one': 2, 'two': 3, 'three': 3, 'four': 2, 'five': 5, 'six': 6, 'seven': 4, 'eight': 5}
nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4}


def my_sum(kwargs):
    k = 0
    sum1, sum2 = 0, 0
    for key in kwargs.keys():
        if k <int(len(kwargs) / 2):
            k += 1
            sum1 += kwargs[key]
        else:
            sum2 += kwargs[key]
    return sum1, sum2


print('Сумма первой половины: {}, второй {}'.format(*my_sum(nums)))
print('Сумма первой половины: {}, второй {}'.format(*my_sum(nums2)))
