# Из предложенного текстового файла (text18-4.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить текст в стихотворной форме предварительно заменив символы верхнего
# регистра на нижний.

with open('text18-4.txt', 'r+', encoding='utf-8') as text:
    main_text = text.read()
    print(main_text, end='\n\n')
    print(len([i for i in main_text if i.isalpha()]))

for i in main_text:
    if i.isupper():
        main_text = main_text.replace(i, i.lower())

print(main_text)

with open('new_text.txt', 'w+', encoding='utf-8') as main:
    for i in main_text.split('\n'):
        main.writelines(f"{i}\n")