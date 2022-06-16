# Возврат ряда Фибоначчи.

def Vozv(num, a=1, b=1):
    if num <= 1:
        return [a]
    return [a] + Vozv(num - 1, a=b, b=b+a)


print(Vozv(6))