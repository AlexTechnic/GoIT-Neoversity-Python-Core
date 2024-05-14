"""
У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. 
Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

Наприклад:

Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000

Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.

Вимоги до завдання:

Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.

Рекомендації для виконання:

Використовуйте менеджер контексту with для читання файлів.
Пам'ятайте про встановлення кодування при відкриті файлів
Для розділення даних у кожному рядку можна застосувати метод split(',').
Обрахуйте загальну суму заробітної плати, а потім розділіть її на кількість розробників, щоб отримати середню зарплату.
Опрацьовуйте можливі винятки при роботі з файлами, такі як відсутність файлу.

Критерії оцінювання:

Функція повинна точно обчислювати загальну та середню суми.
Повинна бути обробка випадків, коли файл відсутній або пошкоджений.
Код має бути чистим, добре структурованим і зрозумілим.

Приклад використання функції:

total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

Очікуваний результат:

Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000
"""


from pathlib import Path


def total_salary(file_path: str) -> tuple:
    """
    Calculates the total and average salaries from a file listing developers' salaries.
    
    Parameters:
    file_path (str): The path to the file containing salary data.
    
    Returns:
    tuple: A tuple containing the total sum of salaries and the average salary.
    
    Raises:
    FileNotFoundError: If the specified file does not exist.
    ValueError: If there are formatting errors in the file data.
    """
    path = Path(file_path)
    
    # Ensure the file exists to prevent FileNotFoundError
    if not path.exists():
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    total_salaries = 0  # Initialize empty values
    developer_counter = 0
    
    # Using context manager to ensure the file is properly closed after reading
    with path.open('r', encoding='utf-8') as salary_file:
        for line in salary_file:
            # Split each line by comma to separate developer names from their salaries
            parts = line.strip().split(',')
            if len(parts) != 2:
                raise ValueError(f"Incorrect format: '{line.strip()}'. Each line must contain a name and a salary, separated by comma.")
            
            # Convert the salary from string to integer
            try:
                salary = int(parts[1])
            except ValueError:
                raise ValueError(f"Invalid salary value: '{line.strip()}'. Salary must be an integer.")
            
            total_salaries += salary
            developer_counter += 1

    if developer_counter == 0:
        raise ValueError("The file is empty. No data to process.")
    
    # Calculate the average salary
    average_salary = total_salaries / developer_counter if developer_counter else 0
    return (total_salaries, average_salary)

# Example usage of the function
if __name__ == "__main__":
    file_path = "salaries_db.txt"  # Assume this file is in the program's root directory
    try:
        total, average = total_salary(file_path)
        print(f"Total salary amount: {total}, Average salary: {int(average)}")
    except Exception as e:
        print(f"Error: {e}")
# END
