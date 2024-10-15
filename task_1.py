"""
 Функція total_salary(path) аналізує файл salary.txt і повертає загальну та середню суму
 заробітної плати всіх розробників.
 Функція total_salary(path) приймає один аргумент - шлях до файлу salary.txt
 Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої
 заробітної плати.
 """

import os
import pathlib

# відкрити файл на считку
# перебрати кожну строку файлу через цикл та додати в результуючий список
# розділити  по комі
# скласти всі значення за індексом
# порахувати кількість ітерацій
# спіймати помилку


def total_salary(path):
    try:
        with open(path, "r", encoding='utf-8') as file:
            sum = 0
            score = 1
            line = file.readline().strip()
            while line:
                sum += int(line.split(",")[1])
                line = file.readline().strip()
                score += 1
        return (sum, int(sum/score))
    except FileNotFoundError:
        print(f'File "{path}" is not exist')
        return 'Error'


total, average = total_salary('goit-pycore-hw-04/salary.txt')
print(f'Total salary is: {total}, average salary is: {average}')
