from command_handler import *


def parse(text):
    tokens = text.strip().split()
    function_name = tokens[0].lower().replace("-", "_")
    if function_name == ".":
        return False
    elif function_exists(function_name):
        params = ",".join([f"'{t}'" for t in tokens[1:]])
        return eval(f"{function_name}({params})")
    else:
        raise KeyError(f"Unknown command: {function_name}")


def function_exists(name):
    try:
        eval(name)
        return True
    except (NameError, SyntaxError):
        return False
