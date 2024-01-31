class Field:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self._value