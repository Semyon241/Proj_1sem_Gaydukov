def bukvi(s):
    for i in s:
        if i.isalpha():
            yield i


st = input("Введите строку: ")
stroka = list(st)

print('Ваша строка :', stroka)

rezult = []

generator = bukvi(stroka)

for j in generator:
    rezult.append(j)
print('Ваша строка без цифр: ', rezult)

