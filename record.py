from name import Name
from phone import Phone


class Record:
    def __init__(self, name):
        if not name:
            raise ValueError(f"'name' is empty or none")
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def update_phone(self, old_phone, new_phone):
        phone = self.find_phone(old_phone)
        if phone:
            phone.value = new_phone.value
            return True
        return False

    def delete_phone(self, phone):
        phone = self.find_phone(phone)
        if phone:
            self.phones.remove(phone)
            return True
        return False

    def find_phone(self, phone_to_find):
        for phone in self.phones:
            if phone == phone_to_find:
                return phone
        return None

    def contains(self, phrase):
        if phrase in self.name.value.lower():
            return True
        for phone in self.phones:
            if phrase in phone.value:
                return True
        return False