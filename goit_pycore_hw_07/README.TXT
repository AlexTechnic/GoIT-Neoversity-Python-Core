A simple CLI bot v. 0.1. 
To run the CLI bot, execute main.py script in the terminal - [python /path/to/main.by]

Structure of the CLI bot project directory

CLI bot project
├── main.py                      (script to run bot as package)
├── bot/                         (bot files directory)
│   ├── __init__.py              (package file)
│   ├── bot.py                   (main bot script)
│   ├── contact_book.py          (contact-book module)
│   ├── errors_decorators.py     (errors decorators)
└── README.TXT                   (you are here)

bot supported commands:

help - general help about bot supported commands
hello - greet the user and ask for a command
add - add a new contact or update an existing one with a phone number
change - change a contact's phone number 
phone - show a contact's phone numbers 
all - show all contacts in the address book
add-birthday - add a birthday to a contact 
show-birthday - show a contact's birthday 
birthdays - show upcoming birthdays 
close or exit - close the bot
