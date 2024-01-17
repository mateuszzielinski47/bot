class AddressBookIterator:
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        self.current = None

    def __iter__(self):
        self.current=self.minimum
        return self

    def __next__(self):
        if self.current==self.maximum:
            raise StopIteration
        result=self.current
        self.current+=1
        return result


if __name__ == '__main__':
    i = AddressBookIterator(1, 100)
    for number in i:
        print(number)
    '''__iterator = i.__iter__()
        while True:
        try:
            number = _iterator.__next_()
            print(number)
        except StopIteration:
            break
    '''