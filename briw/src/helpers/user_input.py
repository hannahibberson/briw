def get_input(message):
    return input(message)

def user_input(validation_check, message, get_input = get_input):
    valid = False
    while not valid:
        i = get_input(message)
        try:
            valid = validation_check(i)
        except:
            raise Exception(f"The validation function was unable to process the given user input. Please add a way to process user inputs such as \"{i}\".")
    return i

def list_validation():
    # Validation that the user input is one of the list members.
    pass

def range_validation():
    # Validation that the user input is an integer value in a given range.
    pass