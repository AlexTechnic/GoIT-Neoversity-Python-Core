"""
Завдання 3


Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, 
виводячи імена всіх піддиректорій та файлів. Для кращого візуального сприйняття, 
імена директорій та файлів мають відрізнятися за кольором.


Вимоги до завдання:

Створіть віртуальне оточення Python для ізоляції залежностей проекту.

Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, 
структуру якої потрібно відобразити.

Використання бібліотеки colorama для реалізації кольорового виведення.

Скрипт має коректно відображати як імена директорій, так і імена файлів, 
використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).

Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.


Рекомендації для виконання:

Спочатку встановіть бібліотеку colorama. Для цього створіть та активуйте віртуальне оточення Python, 
а потім встановіть пакет за допомогою pip.

Використовуйте модуль sys для отримання шляху до директорії як аргументу командного рядка.

Для роботи з файловою системою використовуйте модуль pathlib.

Забезпечте належне форматування виводу, використовуючи функції colorama.


Критерії оцінювання:

Створення та використання віртуального оточення.

Правильність отримання та обробки шляху до директорії.

Точність виведення структури директорії.

Коректне застосування кольорового виведення за допомогою colorama.

Якість коду, включаючи читабельність, структурування та коментарі.


Приклад використання:

Якщо виконати скрипт та передати йому абсолютний шлях до директорії як параметр.

python hw03.py /шлях/до/вашої/директорії

Це призведе до виведення в терміналі списку всіх піддиректорій та файлів у вказаній директорії з використанням 
різних кольорів для піддиректорій та файлів, що полегшить візуальне сприйняття файлової структури.
"""


import sys
from pathlib import Path
# To use colorama, you need to install it first using pip. Better to use virtual environment
from colorama import Fore, Style, init


def print_directory_contents(path, indent_level=0):
    """
    Recursively prints the contents of a directory colored differently for directories and files.
    
    Parameters:
    path (Path): The directory path.
    indent_level (int): Current indentation level for printing hierarchy.
    """
    try:
        if not path.exists():
            print(f"{Fore.RED}Error: The path {path} does not exist.{Style.RESET_ALL}")
            return
        if not path.is_dir():
            print(f"{Fore.RED}Error: The path {path} is not a directory.{Style.RESET_ALL}")
            return

        # Print directory name
        print(f"{' ' * 2 * indent_level}{Fore.BLUE}{path.name}/{Style.RESET_ALL}")

        for item in sorted(path.iterdir()):
            if item.is_dir():
                # Recursive call for directories
                print_directory_contents(item, indent_level + 1)
            else:
                # Print file name
                print(f"{' ' * 2 * (indent_level + 1)}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    init()  # Initialize Colorama
    
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python {sys.argv[0]} <path_to_directory>{Style.RESET_ALL}")
    else:
        directory_path = Path(sys.argv[1])
        print_directory_contents(directory_path)


# END
