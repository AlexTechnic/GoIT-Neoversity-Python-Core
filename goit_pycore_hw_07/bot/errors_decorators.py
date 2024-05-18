"""Module for input error decorator where it handles errors for the command input"""


# Decorator for input errors
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f"Input error: {e}"
        except ValueError as e:
            return f"Input error: {e}"
        except IndexError:
            return "Input error 3: Please, provide enough arguments."
        except Exception as e:
            return f"Input error: {e}"
    return inner
