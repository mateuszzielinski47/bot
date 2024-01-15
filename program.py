import sys
import command_parser
from address_book import AddressBook
from input_error import input_error
from record import Record


@input_error
def process():
    text = input(">>> ")
    result = command_parser.parse(text)
    if type(result) is bool and not result:
        return False
    if type(result) is list:
        for item in result:
            print(item)
    else:
        print(result)
    return True


def main():
    r = Record("Józek")
    print()
    while True:
        if not process():
            break
    print("Good bye!")
    return 0


if __name__ == '__main__':
    sys.exit(main())
