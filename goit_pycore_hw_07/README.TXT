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

[hello] - greet the user and ask for a command
[add] [name] [phone] - add a new contact or update an existing one with a phone number
[delete] [name] - delete the specified contact
[change] [name] [phone] - change a contact's phone number
[phone] [name] - show a contact's phone numbers
[all] - show all contacts in the address book
[add-birthday] [name] [DD.MM.YYYY] - add a birthday date to a contact
[show-birthday] [name] - show a contact's birthday
[birthdays] - show upcoming birthdays
[close] or [exit] - close the bot
