""" This module contains classes for working with a contact book. """


from collections import UserDict
from datetime import datetime, timedelta


class Field:  # Base class for all fields in the contact book
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        super().__init__(value.strip().title())

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(self.value)

class Record:  # Class for a single contact record in the address book 
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        target = None
        for p in self.phones:
            if p.value == phone:
                target = p
                break
        if target:
            self.phones.remove(target)
            return True
        return False

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return True
        return False

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def __str__(self):  # Return string representation of the contact record
        phones = '; '.join(p.value for p in self.phones)  # Join the phone numbers with a semicolon
        birthday = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "N/A"  # Format the birthday as "DD.MM.YYYY" if it exists
        return f"Contact name: {self.name.value}, phones: {phones}, birthday: {birthday}"

class AddressBook(UserDict):  # Class for the address book itself
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False

    def get_upcoming_birthdays(self, days=7):  # Return list of contacts with birthdays in the next "days" days 
        today = datetime.today()
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birthday:
                next_birthday = record.birthday.value.replace(year=today.year)
                if today <= next_birthday <= today + timedelta(days=days):
                    upcoming_birthdays.append(record)
        return upcoming_birthdays