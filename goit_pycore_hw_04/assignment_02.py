"""
Завдання 2

У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, 
його ім'я та вік, розділені комою. Наприклад:

60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5

Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.

Вимоги до завдання:

Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
Функція має повертати список словників, де кожен словник містить інформацію про одного кота.

Рекомендації для виконання:

Використовуйте with для безпечного читання файлу.
Пам'ятайте про встановлення кодування при відкриті файлів
Для кожного рядка в файлі використовуйте split(',') для отримання ідентифікатора, імені та віку кота.
Утворіть словник з ключами "id", "name", "age" для кожного кота та додайте його до списку, який буде повернуто.
Опрацьовуйте можливі винятки, пов'язані з читанням файлу.

Критерії оцінювання:

Функція має точно обробляти дані та повертати правильний список словників.
Повинна бути належна обробка винятків і помилок.
Код має бути чистим, добре структурованим і зрозумілим.

Приклад використання функції:

cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)

Очікуваний результат:

[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
"""


from pathlib import Path


def get_cats_info(file_path: str) -> list:
    """
    Reads a file containing data about cats and returns a list of dictionaries
    with each dictionary containing information about a single cat.
    
    Parameters:
    file_path (str): The path to the text file containing cat data.
    
    Returns:
    list: A list of dictionaries, each containing 'id', 'name', and 'age' of a cat.
    
    Raises:
    FileNotFoundError: If the specified file does not exist.
    ValueError: If there is an issue with the data format in the file.
    """
    path = Path(file_path)
    
    # Check if the file exists to avoid FileNotFoundError
    if not path.exists():
        raise FileNotFoundError(f"The file at {file_path} does not exist.")
    
    cats_info = []
    
    # Using context manager to ensure the file is properly closed after reading
    with path.open('r', encoding='utf-8') as db_file:
        for line in db_file:
            # Split each line by comma to parse cat data
            parts = line.strip().split(',')
            if len(parts) != 3:
                raise ValueError(f"File format is incorrect. Each line must contain an ID, name, and age separated by commas.\n \
                                 Problem line: {line.strip()}")
            
            # Create dict for cats
            cat_dict = {
                "id": parts[0],
                "name": parts[1],
                "age": parts[2]  # Storing age as a string to match the expected output exactly.
            }
            cats_info.append(cat_dict)

    return cats_info

# Example of usage
if __name__ == "__main__":
    file_path = "cats_db.txt"
    try:
        cats_info = get_cats_info(file_path)
        print(cats_info)
    except Exception as e:
        print(f"Error: {e}")


# END
