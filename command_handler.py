from address_book import AddressBook
from phone import Phone
from record import Record

def add_contact(name, *phones):
    r=Record(name)
    for phone in phones:
        r.add_phone(phone)
    contacts.add_record(r)

contacts = AddressBook()

add_contact("Janko Walski", "123-456-789", "444 444 444" )
add_contact("Janka Walska", "555 555 555")
add_contact("Anna Kowalska", "111-222-333", "555 555 555")
add_contact("Bartek Nowak", "444-555-666")
add_contact("Czesław Michalski", "777-888-999", "123 456 789")
add_contact("Dorota Adamczyk", "222-333-444")
add_contact("Ewa Nowakowska", "555-666-777", "987 654 321")
add_contact("Filip Jankowski", "111-333-555")
add_contact("Grażyna Wójcik", "999-888-777", "333 222 111")
add_contact("Henryk Nowacki", "444-555-666")
add_contact("Izabela Wrona", "777-666-555", "111 222 333")
add_contact("Janusz Kozłowski", "888-777-666")


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


# Janko Walski 123456789 111111111
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


def find(*args):
    result = []
    tested_value = " ".join(args).lower()
    for name, record in contacts.items():
        if record.contains(tested_value):
            result.append(f"{name} -> {record.phones}")
    return result


def show_all(*args):
    result = []
    for name, record in contacts.items():
        result.append(f"{name} -> {record.phones}")
    return result


def good_bye(*args):
    return False


def close(*args):
    return False


def exit(*args):
    return False
