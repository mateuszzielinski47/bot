def input_error(function):
    def inner(*args, **kwargs):
        while True:
            try:
                return function(*args, **kwargs)
            except (KeyError, ValueError, IndexError) as e:
                print(e)
    return inner
