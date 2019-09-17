def get_input(message):
    return input(message)

def user_input(check_valid, message, get_input = get_input):
    valid = False
    while not valid:
        i = get_input(message)
        try:
            valid = check_valid(i)
        except:
            raise Exception(f"The validation function was unable to process the given user input. Please add a way to process user inputs such as \"{i}\".")
    return i