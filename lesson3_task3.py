#3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Результат-сумма двух наибольших аргументов - {my_func(int(input("Введите, пожалуйста, первое число ")), int(input("Введите, пожалуйста, второе число ")), int(input("Введите, пожалуйста, третье число ")))}')
