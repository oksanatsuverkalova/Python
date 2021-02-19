#2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк,
# выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('task2.txt') as f:
    lines = f.readlines()
print('Количество строк файла: ', len(lines))
for num_line, line in enumerate(lines, start=1):
    print('{} строка содержит: {} слов(о) '.format(num_line, len(line.split())))