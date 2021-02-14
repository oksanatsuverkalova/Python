#2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
#Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
#Результат: [12, 44, 4, 10, 78, 123].

task_list = [4, 5, 8, 34, 65, 87, 61, 2, 19, 3, 27]
new_list = [num for i, num in enumerate(task_list) if num > task_list[i - 1] and i != 0]
print(f'Исходный список чисел {task_list}')
print(f'Новый список чисел {new_list}')
