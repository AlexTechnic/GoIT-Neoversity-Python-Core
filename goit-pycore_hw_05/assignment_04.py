"""
Assignment 04 - CLI assistant bot + decorators
"""

# examples of user inputs:
# add John 1234567890
# change John 9876543210
# phone John
# all

# Defining decorator function
def input_error(func): 
    """ Decorator to handle input errors in command functions."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found." # in case of user input unknown contact name, example: phone John (John not exist)
        except ValueError:
            return "Error: Please enter a valid name and phone number." # in case of invalid number of arguments, example: add John (missing number)
        except IndexError:
            return "Error: Please provide enough arguments." # in case of not enough arguments, for example: add (no arguments provided)
    return inner

@input_error # Decorator to handle input error of add_contact function
def add_contact(args, contacts):
    """ Add a contact to the contacts dictionary with a name and phone number."""
    if len(args) != 2:
        raise ValueError("Invalid number of arguments.")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error # Decorator to handle input error of change_contact function
def change_contact(args, contacts):
    """ Change an existing contact's phone number in the contacts dictionary."""
    if len(args) != 2:
        raise ValueError("Invalid number of arguments.")
    name, phone = args
    if name not in contacts:
        raise KeyError("Contact does not exist.")
    contacts[name] = phone
    return "Contact updated."

@input_error # Decorator to handle input error of show_phone function
def show_phone(args, contacts):
    """ Display the phone number of a specified contact."""
    if len(args) != 1:
        raise ValueError("Invalid number of arguments.")
    name = args[0]
    if name not in contacts:
        raise KeyError("Contact does not exist.")
    return f"{name}'s phone number is {contacts[name]}"

def show_all(contacts):
    """ Display all contacts stored in the contacts dictionary."""
    if not contacts:
        return "No contacts stored."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

# Function to parse the user input into a command and arguments 
def parse_input(user_input):
    """
    Parse the user input into a command and arguments.
    """
    parts = user_input.strip().split(maxsplit=2)
    command = parts[0].lower()
    args = parts[1:] if len(parts) > 1 else []
    return command, args

# Main function to run the CLI assistant bot
def main():
    contacts = {}
    print("Welcome to the CLI Assistant Bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        # Check the command and call the appropriate function
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

# Run the main function when the script is executed from the command line 
if __name__ == "__main__":
    main()

# END
