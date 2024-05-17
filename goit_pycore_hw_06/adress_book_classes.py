# simple adress book classes template
# this is a simple address book classes template that can store contacts with names and phone numbers 
# and perform basic operations on them


from collections import UserDict


# Field class is a base class for Name and Phone classes that represent contact name and phone number respectively
class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):  # returns a string representation of the field
        return str(self.value)


# Name class represents contact name
class Name(Field):
    pass


# Phone class represents contact phone number
class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)


# Record class represents a contact with name and phone numbers and can perform basic operations on them
class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):  # raises ValueError if phone is not valid
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):  # returns True if phone was found and removed, False otherwise
        target = None
        for p in self.phones:
            if p.value == phone:
                target = p
                break
        if target:
            self.phones.remove(target)
            return True
        return False

    def edit_phone(self, old_phone, new_phone):  # returns True if phone was found and updated, False otherwise
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return True
        return False

    def find_phone(self, phone):  # returns Phone object if found, None otherwise
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):  # returns a string representation of the contact
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


# AddressBook class represents a collection of contacts and can perform basic operations on them 
# (like adding, finding and deleting contacts)
class AddressBook(UserDict):
    def add_record(self, record):  # adds a new contact to the address book
        self.data[record.name.value] = record

    def find(self, name):  # returns Record object if found, None otherwise
        return self.data.get(name)

    def delete(self, name):  # returns True if contact was found and deleted, False otherwise
        if name in self.data:
            del self.data[name]
            return True
        return False
