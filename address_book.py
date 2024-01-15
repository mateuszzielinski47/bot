from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find_record_by_name(self, value):
        for name, record in self.items():
            if name == value:
                return record
        return None
