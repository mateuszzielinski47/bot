import re

from field import Field


class Phone(Field):
    def __init__(self, value):
        Field.__init__(self, self.__format_number(value))

    def __repr__(self):
        return self.value

    def __format_number(self, value):
        return re.sub(r'\D', '', value)
