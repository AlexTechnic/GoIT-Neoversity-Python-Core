"""
Assignment 04 - CLI assistant bot - look assignment_04_readme.txt for more information.

"""


# BEGIN


def parse_input(user_input):
    """
    Parse the user input into a command and arguments.
    
    Parameters:
        user_input (str): The raw input string from the user.
    
    Returns:
        tuple: A tuple containing the command (str) and a list of arguments (list).
    """
    parts = user_input.strip().split(maxsplit=2)  # Remove extra spaces and split the input into parts
    command = parts[0].lower()  # Get the command, converting it to lowercase for ease of comparison
    args = parts[1:] if len(parts) > 1 else []  # Get the arguments if they exist
    return command, args

def add_contact(args, contacts):
    """
    Add a contact to the contacts dictionary with a name and phone number.
    
    Parameters:
        args (list): A list containing the name and phone number.
        contacts (dict): The dictionary to store contact information.
    
    Returns:
        str: A message indicating the outcome of the operation.
    """
    if len(args) != 2:
        return "Error: Please enter a valid name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Change an existing contact's phone number in the contacts dictionary.
    
    Parameters:
        args (list): A list containing the name and new phone number.
        contacts (dict): The dictionary containing contact information.
    
    Returns:
        str: A message indicating the outcome of the operation.
    """
    if len(args) != 2:
        return "Error: Please enter a valid name and new phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error: Contact not found."

def show_phone(args, contacts):
    """
    Display the phone number of a specified contact.
    
    Parameters:
        args (list): A list containing the contact's name.
        contacts (dict): The dictionary containing contact information.
    
    Returns:
        str: A message indicating the contact's phone number or an error message.
    """
    if len(args) != 1:
        return "Error: Please enter a valid name."
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        return "Error: Contact not found."

def show_all(contacts):
    """
    Display all contacts stored in the dictionary.
    
    Parameters:
        contacts (dict): The dictionary containing contact information.
    
    Returns:
        str: A formatted string of all contacts and their phone numbers or a message indicating no contacts are stored.
    """
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts stored."

def main():
    """
    Main function to handle the bot operations.
    """
    contacts = {}
    print("Welcome to the CLI Assistant Bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

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

if __name__ == "__main__":
    main()


# END
