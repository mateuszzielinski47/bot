from field import Field


class Name(Field):
    def __init__(self, value):
        Field.__init__(self, value)

    @Field.value.setter
    def value(self, value):
        self._value = value

    def __repr__(self):
        return self.value
