import random

from address_book import AddressBook
from birthday import Birthday
from phone import Phone
from record import Record


def add_contact(name, *phones):
    r = Record(name)
    for phone in phones:
        r.add_phone(Phone(phone))
    if random.randint(1, 10) == 10:
        year = random.randint(1970, 2024)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        r.birthday = f'{year}-{month:0>2}-{day:0>2}'
    contacts.add_record(r)


contacts = AddressBook()

add_contact("Adam Kowalski", "123-456-789", "444 444 444")
add_contact("Alicja Nowak", "555-555-555")
add_contact("Bartosz Jankowski", "111-222-333", "555 555 555")
add_contact("Beata Wójcik", "444-555-666")
add_contact("Cezary Michalski", "777-888-999", "123 456 789")
add_contact("Dorota Adamczyk", "222-333-444")
add_contact("Ewa Nowakowska", "555-666-777", "987 654 321")
add_contact("Filip Jankowski", "111-333-555")
add_contact("Grażyna Wójcik", "999-888-777", "333 222 111")
add_contact("Henryk Nowacki", "444-555-666")
add_contact("Izabela Wrona", "777-666-555", "111 222 333")
add_contact("Janusz Kozłowski", "888-777-666")
add_contact("Karolina Szymańska", "111-222-333", "555 555 555")
add_contact("Krzysztof Malinowski", "555-555-555")
add_contact("Laura Wojciechowska", "111-222-333", "555 555 555")
add_contact("Łukasz Niedzielski", "444-555-666")
add_contact("Magdalena Szymańska", "777-888-999", "123 456 789")
add_contact("Marcin Jastrzębski", "222-333-444")
add_contact("Natalia Stępień", "555-666-777", "987 654 321")
add_contact("Oskar Lisowski", "111-333-555")
add_contact("Patrycja Piotrowska", "999-888-777", "333 222 111")
add_contact("Piotr Słowikowski", "444-555-666")
add_contact("Renata Kwiatkowska", "123-456-789", "444 444 444")
add_contact("Robert Malinowski", "555-555-555")
add_contact("Sabina Wojciechowska", "111-222-333", "555 555 555")
add_contact("Sebastian Niedzielski", "444-555-666")
add_contact("Teresa Szymańska", "777-888-999", "123 456 789")
add_contact("Tomasz Jastrzębski", "222-333-444")
add_contact("Urszula Stępień", "555-666-777", "987 654 321")
add_contact("Wojciech Lisowski", "111-333-555")
add_contact("Zofia Piotrowska", "999-888-777", "333 222 111")
add_contact("Adam Słowikowski", "444-555-666")
add_contact("Alicja Kowalska", "123-456-789", "444 444 444")
add_contact("Bartłomiej Nowak", "555-555-555")
add_contact("Celina Kowalczyk", "111-222-333", "555 555 555")
add_contact("Dariusz Wiśniewski", "444-555-666")
add_contact("Ewa Michalska", "777-888-999", "123 456 789")
add_contact("Fryderyk Adamczyk", "222-333-444")
add_contact("Gabriela Nowakowska", "555-666-777", "987 654 321")
add_contact("Hubert Jankowski", "111-333-555")
add_contact("Izabela Wójcik", "999-888-777", "333 222 111")
add_contact("Jerzy Nowacki", "444-555-666")
add_contact("Katarzyna Wrona", "777-666-555", "111 222 333")
add_contact("Lech Kozłowski", "888-777-666")
add_contact("Marta Szymańska", "111-222-333", "555 555 555")
add_contact("Norbert Malinowski", "555-555-555")
add_contact("Olga Wojciechowska", "111-222-333", "555 555 555")
add_contact("Piotr Niedzielski", "444-555-666")
add_contact("Renata Szymańska", "777-888-999", "123 456 789")
add_contact("Szymon Jastrzębski", "222-333-444")
add_contact("Teresa Stępień", "555-666-777", "987 654 321")
add_contact("Urszula Lisowska", "111-333-555")
add_contact("Waldemar Piotrowski", "999-888-777", "333 222 111")
add_contact("Zofia Słowikowska", "444-555-666")
add_contact("Adam Kwiatkowski", "123-456-789", "444 444 444")
add_contact("Anna Malinowska", "555-555-555")
add_contact("Bartosz Wojciechowski", "111-222-333", "555 555 555")
add_contact("Beata Niedzielska", "444-555-666")
add_contact("Cezary Szymański", "777-888-999", "123 456 789")
add_contact("Dorota Jastrzębska", "222-333-444")
add_contact("Ewa Stępień", "555-666-777", "987 654 321")
add_contact("Filip Lisowski", "111-333-555")
add_contact("Grażyna Piotrowska", "999 888 777", "333 222 111")
add_contact("Henryk Słowikowski", "444-555-666")


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
    return False


def close(*args):
    return False


def exit(*args):
    return False
