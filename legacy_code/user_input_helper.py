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

def confirm_choice_validation(response):
    if response.lower() == 'n' or response.lower() == 'y':
        return True
    else:
        print("Please enter y/n.")
        return False

def get_user_choice_confirmation(message:str):
    response = user_input(confirm_choice_validation, message)
    if response == "y":
        return True
    else:
        return False
    