import random

from address_book import AddressBook
from birthday import Birthday
from phone import Phone
from record import Record

ADDRESS_BOOK_FILE = "address_book.json"

contacts = AddressBook()
contacts.deserialize(ADDRESS_BOOK_FILE)


def hello(*args):
    return "How can I help you?"


def add(*args):
    name = " ".join(args[0:-1])
    number = Phone(args[-1])
    r = contacts.find_record_by_name(name)
    if not r:
        r = Record(name)
    r.add_phone(number)
    contacts.add_record(r)
    return "[OK]!"


def change(*args):
    tested_name = " ".join(args[0:-2]).lower()
    old_number = Phone(args[-2])
    new_number = Phone(args[-1])
    for name, record in contacts.items():
        if name.lower() == tested_name:
            if record.update_phone(old_number, new_number):
                return "[OK]!"
            else:
                return f"Number not found for '{old_number}'"
    return f"Name not found '{tested_name}'"


def phone(*args):
    tested_name = " ".join(args).lower()
    for name, record in contacts.items():
        if name.lower() == tested_name:
            print(record.phones)
            return "[OK]!"
    return f"Name not found for '{tested_name}'"


def birthday(*args):
    tested_name = " ".join(args[0:-1]).lower()
    date = args[-1]
    for name, record in contacts.items():
        if name.lower() == tested_name:
            record.birthday = date
            return ("[OK]")
    return f"Name not found '{tested_name}'"


def find(*args):
    result = []
    tested_value = " ".join(args).lower()
    for name, record in contacts.items():
        if record.contains(tested_value):
            result.append(f"{name} -> {record.phones}")
    return result


def show_all(*args):
    result = []
    for page in range(contacts.page_count()):
        result.append((f"{'-' * 40} PAGE {page + 1} {'-' * 40}"))
        for record in contacts.iterator(page):
            result.append(f"→ {record.name.value: <35}    {record.phones[0]}")
            for phone in record.phones[1:]:
                result.append(f"  {'':<35}    {phone}")
            if record.birthday:
                result.append(f"  {'':^35}    📅{record.birthday}")
    return result


def good_bye(*args):
    contacts.serialize(ADDRESS_BOOK_FILE)
    return False


def close(*args):
    contacts.serialize(ADDRESS_BOOK_FILE)
    return False


def exit(*args):
    contacts.serialize(ADDRESS_BOOK_FILE)
    return False
