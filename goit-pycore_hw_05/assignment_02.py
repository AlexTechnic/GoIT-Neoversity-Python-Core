
import re  # import regular expression module to check for numbers in text

def generator_numbers(text):
    """This function will return a generator that will return all numbers in the text"""
    for number in re.finditer(r'\b\d+\.?\d*\b', text):  # find all numbers in the text
        yield float(number.group())  # yield the number as a float

def sum_profit(text, func):
    """This function will return the sum of all numbers in the text using the generator function passed as argument"""
    return sum(func(text))

# test of function
text = "Incomes was 250, 60.5, 300 and 500.75"
total_income = sum_profit(text, generator_numbers) 
print(f"Total of income values in text are: {total_income}")  # 1111.25