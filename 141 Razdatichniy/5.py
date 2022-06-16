#Реверсирование числа

def reverse(chi):
    if chi < 10:
        return str(chi)
    shi = chi % 10
    chi //=10
    return str(shi) + reverse(chi)

numb = 456789
print(reverse(numb))