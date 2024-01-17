from datetime import datetime


class Birthday:
    def __init__(self, value):
        self.value = datetime.strptime(value, "%Y-%m-%d")

    def days_to_birthday(self):
        today = datetime.now()
        birthday = datetime(today.year, self.value.month, self.value.day)

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        days_to_birthday = birthday - today
        return days_to_birthday

if __name__=='__main__':
    b= Birthday("2000-01-01")

