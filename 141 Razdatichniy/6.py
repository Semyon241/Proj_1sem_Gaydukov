# Возведение числа x в степень у

def vozv(x, y):
    if y == 0:
        return 1
    return x * vozv(x, y - 1)


x = 3
y = 3
result = vozv(x, y)
print(result)
