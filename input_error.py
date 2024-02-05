def input_error(function):
    def inner(*args, **kwargs):
        while True:
            try:
                return function(*args, **kwargs)
            except (KeyError, ValueError, IndexError, TypeError) as e:
                print(e)
    return inner
