"""
Функція get_cats_info(path) читає файл cats.txt та повертає список словників з інформацією про 
кожного кота.
Функція get_cats_info(path) приймає один аргумент - шлях до текстового файлу (path)
"""
import os
import pathlib

# відкрити файл на считку
# створити змінну із списком ключів
# перебрати кожну строку файлу через цикл
# розділити строчку по комі
# створити змінну з списком значень та передати у змінну результат розділення строчки по комі
# об'єднати ключ - значення
# спіймати помилку


def get_cats_info(path) -> list:
    try:
        with open(path, 'r', encoding='utf-8') as file:
            new_lst = []
            keys = ['id', 'name', 'age']
            line = file.readline().strip()
            while line:
                values = line.split(",")
                new_lst.append(dict(zip(keys, values)))
                line = file.readline().strip()
        return new_lst
    except FileNotFoundError:
        print(f'File "{path}" not found.')
    return 'Error'


cats_info = get_cats_info('goit-pycore-hw-04/cats.txt')
print(cats_info)
