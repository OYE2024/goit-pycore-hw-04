#!/usr/bin/env python

"""
Скрипт приймає шлях до директорії(папки) в якості аргументу командного рядка і візуалізує 
структуру цієї директорії, виводячи імена всіх піддиректорій та файлів.
Імена директорій та файлів відрізняються за кольором.
Якщо вказаний шлях не існує або він не веде до директорії виконується обробка помилки.
"""

import os
from colorama import Fore
import sys


def print_dir(path: str, padding=''):
    try:
        files = os.listdir(path)
        for i in files:
            if os.path.isdir(f'{path}/{i}'):  # перевірка на умову чи є файл пакой
                print(Fore.BLUE+padding+i)
                # додаємо табуляцію до кожної ітерації рекурсії
                print_dir(f'{path}/{i}', padding + '\t')
            else:
                print(Fore.GREEN+padding+i)
    except FileNotFoundError:
        print(f"Error. Folder '{path}' doesn't exist")


# Отримання директорії від користувача та перевірка на наявність аргументу (назва директорії)
if len(sys.argv) <= 1:
    print("No arguments")
else:
    user_path = sys.argv[1]
    print_dir(user_path)
