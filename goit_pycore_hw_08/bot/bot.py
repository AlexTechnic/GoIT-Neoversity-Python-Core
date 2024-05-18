""" A simple CLI bot v.0.2 for managing an address book. 
To run the bot, execute this .py script in the terminal. """

from bot.contact_book import AddressBook, Record
from bot.errors_decorators import input_error

HELP_INFO = "\nCLI bot assistant 'Rezervius++ v.0.123' by Oleksii Lavrenchuk\n\n\
supported input commands:\n\n\
[hello] - greet the user and ask for a command\n\
[add] [name] [phone] - add a new contact or update an existing one with a phone number\n\
[delete] [name] - delete the specified contact\n\
[change] [name] [phone] - change a contact's phone number\n\
[phone] [name] - show a contact's phone numbers\n\
[all] - show all contacts in the address book\n\
[add-birthday] [name] [DD.MM.YYYY] - add a birthday date to a contact\n\
[show-birthday] [name] - show a contact's birthday\n\
[birthdays] - show upcoming birthdays\n\
[save] - save the address book to a .pkl file\n\
[load] - load the address book from a .pkl file\n\
[close] or [exit] - save data and close the bot\n"

def help_command():
    return HELP_INFO

# Function to parse user input
def parse_input(user_input):
    """ Parse the user input into a command and arguments."""
    parts = user_input.strip().split(maxsplit=2)  # Split the input into 3 parts
    command = parts[0].lower()  # The first part is the command (case-insensitive)
    args = parts[1:] if len(parts) > 1 else []  # The rest of the parts are arguments
    return command, args

# Functions to handle user commands
@input_error
def add_contact(args, book: AddressBook):
    """ Add a new contact to the address book."""
    name, phone = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:  # If the contact doesn't exist, create a new record for it
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:  # Add the phone number to the record if provided
        record.add_phone(phone)
    return message

# Function to delete a contact
@input_error
def delete_contact(args, book: AddressBook):
    if len(args) != 1:
        raise ValueError("Please provide a name.")
    name = args[0]
    if book.delete(name):
        return f"Contact {name} deleted."
    else:
        raise KeyError(f"Contact {name} not found.")

# Function to change a contact's phone number
@input_error
def change_contact(args, book: AddressBook):
    """ Change a contact's phone number."""
    name, old_phone, new_phone = args
    record = book.find(name)  # Find the contact in the address book
    if record is None:
        raise KeyError("Contact not found.")
    if not record.edit_phone(old_phone, new_phone):   # Edit the phone number if it exists
        raise ValueError("Old phone number not found.")
    return "Contact updated."

# Function to show a contact's phone numbers
@input_error
def show_phone(args, book: AddressBook):
    """ Show a contact's phone numbers."""
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    return ', '.join(phone.value for phone in record.phones)  # Return the phone numbers as a comma-separated string

# Function to show all contacts
@input_error
def show_all(book: AddressBook):
    """ Show all contacts in the address book."""
    return '\n'.join(str(record) for record in book.data.values())  # Return a string representation of each contact 

# Function to add a birthday to a contact
@input_error
def add_birthday(args, book: AddressBook):
    """ Add a birthday to a contact."""
    name, birthday = args
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    record.add_birthday(birthday)
    return "Birthday added."

# Function to show a contact's birthday
@input_error
def show_birthday(args, book: AddressBook):
    """ Show a contact's birthday."""
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError("Contact not found.")
    if record.birthday:
        return record.birthday.value.strftime("%d.%m.%Y")  # Return the birthday in the format "DD.MM.YYYY" if it exists
    return "Birthday not set."

# Function to show upcoming birthdays
@input_error
def birthdays(book: AddressBook):
    """ Show upcoming birthdays in the address book."""
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No upcoming birthdays."
    
    # Return a string with each upcoming birthday in the format "Name: DD.MM.YYYY"
    return '\n'.join(f"{record.name.value}: {record.birthday.value.strftime('%d.%m.%Y')}" for record in upcoming)

# Main function to run the CLI bot loop
def main():
    book = AddressBook()
    print("Welcome to the CLI Assistant Bot!")
    while True:  # Loop to keep the bot running
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:  # Exit the loop if the user wants to close the bot 
            book.save_to_file()
            print("Data saved. Exiting. Good bye!")
            break

        elif command == "help":
            print(help_command())

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "delete":
            print(delete_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(show_all(book))

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(book))

        elif command == "save":  # Save the address book to a .pkl file
            book.save_to_file()
            print("Contact book successfully saved to .pkl data file.")

        elif command == "load":  # Load the address book from a .pkl file
            book = AddressBook.load_from_file()
            print("Contact book successfully loaded from .pkl data file.")

        else:
            print("Invalid command.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()