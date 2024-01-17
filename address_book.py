from collections import UserDict

DEFAULT_PAGE_SIZE = 10


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find_record_by_name(self, value):
        for name, record in self.items():
            if name == value:
                return record
        return None

    def iterator(self, page):
        pass


if __name__ == "__main__":
    for number in AddressBook().iterator(1, 10):
        print(number)
