"""
Завдання 2

Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в 
певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для 
таких лотерей. Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні 
бути унікальні.

Вимоги до завдання:

Параметри функції:
min - мінімальне можливе число у наборі (не менше 1).
max - максимальне можливе число у наборі (не більше 1000).
quantity - кількість чисел, які потрібно вибрати (значення між min і max).
Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. 
Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.

Рекомендації для виконання:

Переконайтеся, що вхідні параметри відповідають заданим обмеженням.
Використовуйте модуль random для генерації випадкових чисел.
Використовуйте множину або інший механізм для забезпечення унікальності чисел.
Пам'ятайте, що функція get_numbers_ticket повертає відсортований список унікальних чисел.

Критерії оцінювання:

Валідність вхідних даних: функція повинна перевіряти коректність параметрів.
Унікальність результату: усі числа у видачі повинні бути унікальними.
Відповідність вимогам: результат має бути у вигляді відсортованого списку.
Читабельність коду: код має бути чистим і добре документованим.

Приклад: Припустимо, вам потрібно вибрати 6 унікальних чисел для лотерейного квитка, де числа повинні бути у діапазоні від 1 до 49. 
Ви можете використати вашу функцію так:

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

Цей код викликає функцію get_numbers_ticket з параметрами min=1, max=49 та quantity=6. 
В результаті ви отримаєте список з 6 випадковими, унікальними та відсортованими числами, наприклад, [4, 15, 23, 28, 37, 45]. 
Кожен раз при виклику функції ви отримуватимете різний набір чисел.
"""


import random

def get_numbers_ticket(min_num: int, max_num: int, quantity: int) -> list:
    """
    Generates list of unique random numbers in the specified qantity of numbers and within [min-max] range.

    Parameters:
    min_num (int): The min possible number in the set (>1).
    max_num (int): The max possible number in the set (<1000).
    quantity (int): The number of unique numbers to be selected.

    Returns:
    list: unique, random numbers within the specified parameters.
          Returns an empty list if the input parameters are invalid.
    """
    # Check the parameters are valid.
    if not (1 <= min_num <= max_num <= 1000) or not (min_num <= quantity <= max_num):
        return []  # Return an empty list if the parameters are out of bounds.

    # Generate a sorted set of unique random numbers.
    lottery_numbers = sorted(random.sample(range(min_num, max_num + 1), quantity))

    return lottery_numbers


print("This function will generate unique random numbers for a lottery ticket.")

# Input of user parameters for random-generator function
min_num = int(input('Enter min possible integer number (not less than 1):'))
max_num = int(input('Enter max possible integer number (not more than 1000):'))
num_qty = int(input('Enter needed q-ty of numbers (in bounds [min number < q-ty < max number]):'))

lottery_numbers = get_numbers_ticket(min_num, max_num, num_qty)

print(f"Your {num_qty} random unique numbers in range [{min_num}:{max_num}] are: {lottery_numbers}.")

# END
