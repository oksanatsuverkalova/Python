# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('task1.txt', 'w') as f:
    while True:
        line = input ('Введите, пожалуйста, строку.Окончание ввода данных - пустая строка: ')
        if line == '':
            break
        f.write(line + '\n')