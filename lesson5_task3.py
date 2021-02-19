# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

with open('task3.txt') as f:
    lines = f.readlines()

    allsalary = []
    for line in lines:
        surname, salary = line.split(' - ')
        allsalary.append(int(salary))
        if int(salary) < 20000:
            print(line, end='')
        print('\nСредняя величина заработной платы сотрудников:', sum(allsalary) / len(allsalary))