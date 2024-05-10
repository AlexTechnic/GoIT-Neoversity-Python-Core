"""
Завдання 1

Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

Вимоги до завдання:

Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, 
результат має бути від'ємним. У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
Для роботи з датами слід використовувати модуль datetime Python.

Рекомендації для виконання:

Імпортуйте модуль datetime.
Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
Отримайте поточну дату, використовуючи datetime.today().
Розрахуйте різницю між поточною датою та заданою датою.
Поверніть різницю у днях як ціле число.

Критерії оцінювання:

Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
Читабельність коду: код повинен бути чистим і добре документованим.

Приклад:

Якщо сьогодні 5 травня 2021 року, виклик get_days_from_today("2021-10-09") повинен повернути 157, 
оскільки 9 жовтня 2021 року є на 157 днів пізніше від 5 травня 2021 року.
"""


""""
Script contains function 'get_days_from_today(date)' that calculates the number of days
between a specified date and the current date. It uses the 'datetime' module for date calculations
and the 're' module to validate the input format with Regular Expressions.
"""


import datetime
import re


def get_days_from_today(date_str: str) -> int:
    """
    Calculates the number of days from a given date to today's date using datetime lib.

    Parameters:
    date_str (str): The date string entered by user in the format 'YYYY-MM-DD'.

    Returns:
    int: The whole number of days between the given date and today, 
    positive number if the date is in the past, negative if in the future.

    Raises:
    ValueError: If the input date_str is not a valid date or not in the correct format, it raises error from datetime lib.
    """
    # Attempt to convert the input string into a 'datetime.date' object.
    given_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

    # Get today's date from the 'datetime' module.
    today_date = datetime.date.today()

    # Calculate the difference between the given date and today.
    delta = today_date - given_date

    # Return the whole number of days.
    return delta.days


# Using RegEx pattern to check YYYY-MM-DD syntax format.
date_pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")

print("This program calculates the number of days from a given date to today.")
print("Please enter a date in the format 'YYYY-MM-DD' (e.g., '2023-01-01').")

# Start an infinite loop until a valid value of date is entered.
while True:
    user_date = input("Please enter a date: ")
    # Check if the user input matches the expected date format.
    if not date_pattern.match(user_date):
        print("Invalid date. Invalid syntax format. Please re-enter in YYYY-MM-DD format.")  # Inform the user if the input format is incorrect.
        continue  # Skip the rest of the loop and ask for input again.
    try:
        # Call the function with the users input and print the result.
        days_difference = get_days_from_today(user_date)
        print(f"Days from the given date to today: {days_difference}")
        break  # Exit the loop if the date is valid and processed.
    except ValueError as date_value_error:
        # Catch and handle the ValueError if the date is invalid (like 2000-13-33, or etc.).
        print(f"Invalid date. This date not exist in calendar. Please re-enter a valid date.")

# END
