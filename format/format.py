import re

def number_formatting(number):
    formated_number=re.sub(r'\D', '', number)
    return formated_number
