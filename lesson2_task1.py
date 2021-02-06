# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

task1_int = 23
task1_str = "Times are changing"
task1_float = 1.7
task1_list = ['56', '3', 'abc', 7, '32', 'qwerty', 15, 90]
task1_tuple = [4, 8, 15, 16, 23, 42]
task1_set = {True, 67, 'world', 12, None}
task1_dict = {'city': 'Moscow', 'country': 'Russia'}

lesson2_list = [task1_int, task1_str, task1_float, task1_list, task1_tuple, task1_set, task1_dict]
for i in lesson2_list:
    print(f'{i} is {type(i)}')
