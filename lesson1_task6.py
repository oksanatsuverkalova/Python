#Спортсмен занимается ежедневными пробежками.
#В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
# Требуется определить номер дня,
# на который результат спортсмена составит не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
#1-й день: 2
#2-й день: 2,2
#3-й день: 2,42
#4-й день: 2,66
#5-й день: 2,93
#6-й день: 3,22
#Ответ: на шестой день спортсмен достиг результата — не менее 3 км.

dist_a = int(input('Пожалуйста, введите результат пробежки спортсмена за первый день, км: '))
dist_b = int(input('Пожалуйста, введите желаемый результат пробежки спортсмена, км: '))

i = 1
while dist_a < dist_b:
    dist_a += dist_a / 10
    i += 1

print(f'На {i}-й день спортсмен достиг результата — не менее {dist_b} км')