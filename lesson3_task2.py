# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def func_task2(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(func_task2(name='Иван',surname='Иванов', year='1990', city='Тула', email='ivanov@mail.ru',
              telephone='8-900-300-00-99'))