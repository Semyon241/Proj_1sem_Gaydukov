# Дана строка-предложение. Зашифровать ее, поместив вначале все символы,
# расположенные на четных позициях строки, а затем, в обратном порядке, все
# символы, расположенные на нечетных позициях (например, строка «Программа»
# превратится в «ргамамроП»).

s = 'БигМак'
print(f'{s[1::2]}{s[::2]}'' - слово, полученное при расположении сначала четных символов, затем нечетных.')