import re

from field import Field


class Phone(Field):
    def __init__(self, value):
        Field.__init__(self, value)

    @Field.value.setter
    def value(self, value):
        value = self.__format_number(value)
        if not re.fullmatch(r"\d{9}", value):
            raise ValueError("Phone nuber is invalid format!")
        self._value = value

    def __repr__(self):
        return self.value

    def __format_number(self, value):
        return re.sub(r'\D', '', value)



