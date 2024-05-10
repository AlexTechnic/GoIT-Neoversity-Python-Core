"""
Завдання 4

У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес, вам потрібно 
створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати. Функція повинна повернути список 
всіх у кого день народження вперед на 7 днів включаючи поточний день.

У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день народження. Оскільки 
дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це та переносити дату привітання на наступний 
робочий день, якщо необхідно.

Вимоги до завдання:

Параметр функції users - це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) 
та birthday (день народження, рядок у форматі 'рік.місяць.дата').

Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, 
дата привітання переноситься на наступний понеділок.

Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання 
(ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').

Рекомендації для виконання:

Припускаємо, що ви отримали список users, де кожен словник містить name (ім'я користувача) та birthday (дата народження у форматі 
рядка 'рік.місяць.дата'). Ви повинні перетворити дати народження з рядків у об'єкти datetime. Конвертуйте дату народження із рядка 
у datetime об'єкт - datetime.strptime(user["birthday"], "%Y.%m.%d").date(). Оскільки потрібна лише дата (без часу), 
використовуйте .date() для отримання тільки дати.

Визначте поточну дату системи за допомогою datetime.today().date().

Пройдіться по списку users та аналізуйте дати народження кожного користувача (for user in users:).

Перевірте, чи вже минув день народження в цьому році (if birthday_this_year < today). Якщо так, розгляньте дату на наступний рік.

Визначте різницю між днем народження та поточним днем для визначення днів народження на наступний тиждень.
Перевірте, чи день народження припадає на вихідний. Якщо так, перенесіть дату привітання на наступний понеділок.
Створіть структуру даних, яка зберігатиме ім'я користувача та відповідну дату привітання, якщо день народження відбувається протягом наступного тижня.
Виведіть зібрані дані у вигляді списку словників з іменами користувачів та датами привітань.

Критерії оцінювання:

Актуальність та коректність визначення днів народження на 7 днів вперед.
Правильність обробки випадків, коли дні народження припадають на вихідні.
Читабельність та структурованість коду.

Приклад:

Припустимо, у вас є список users:

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

Використання функції get_upcoming_birthdays:

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

Якщо сьогодні 2024.01.22 результатом може бути:

[
    {'name': 'John Doe', 'congratulation_date': '2024.01.23'}, 
    {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
]

Цей список містить інформацію про те, кого і коли потрібно привітати з днем народження.
"""


import datetime


def get_upcoming_birthdays(users):
    """
    Returns a list of co-workers whose birthdays will be in the next 7 days, including today.
    If a birthday falls on a weekend, it shifts to the next Monday.

    Parameters:
    users (list): A list of dictionaries (as 'database' or 'array') containing 'name' and 'birthday' values as keys.

    Returns:
    list: A list of dictionaries with 'name' and 'congratulation_date' values as keys.
    """
    # Get today's date object
    today = datetime.date.today()

    # Initialize list for upcoming birthdays
    upcoming_birthdays = []

    # Iterate through users list to check each birthday
    for user in users:
        # Parse the birthday into a date object
        birthday = datetime.datetime.strptime(user['birthday'], "%Y.%m.%d").date()

        # Calculate the birthday for the current year
        birthday_this_year = birthday.replace(year=today.year)

        # If the birthday has already passed this year, consider it for the next year
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Calculate the difference in days from today
        days_until_birthday = (birthday_this_year - today).days

        # Check if the birthday is within the next 7 days
        if 0 <= days_until_birthday <= 7:
            # If the birthday on a weekend, move it to the next Monday
            if birthday_this_year.weekday() == 5:  # Saturday
                congratulation_date = birthday_this_year + datetime.timedelta(days=2)
            elif birthday_this_year.weekday() == 6:  # Sunday
                congratulation_date = birthday_this_year + datetime.timedelta(days=1)
            else:
                congratulation_date = birthday_this_year

            # Adding to the list of upcoming birthdays
            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


# Database of users birthdays
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Alice Johnson", "birthday": "1995.01.25"},
    {"name": "Bob Brown", "birthday": "1980.01.21"},
    {"name": "Testman X", "birthday": "1991.05.13"},
]

# Usage: upcoming birthdays for the next 7 days
upcoming_birthdays = get_upcoming_birthdays(users)
print("Upcoming birthdays in the next 7 days:", upcoming_birthdays)

# END
