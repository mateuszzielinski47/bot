from datetime import datetime
from field import Field
import re


class Birthday(Field):
    def __init__(self, value):
        Field.__init__(self, value)

    @Field.value.setter
    def value(self, value):
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
            raise ValueError("Birthday has invalid format!")
        self._value = datetime.strptime(value, "%Y-%m-%d")

    def days_to_birthday(self):
        today = datetime.now()
        birthday = datetime(today.year, self.value.month, self.value.day)

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        days_to_birthday = birthday - today
        return days_to_birthday

if __name__=="__main__":
    b = Birthday("2000-01-aa")
    print(b.value)