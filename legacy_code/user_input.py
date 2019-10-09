def getCommand():
    command = input("\nOption number: ")
    try:
        return int(command)
    except:
        print("Please enter an integer value from the list above.")
        return getCommand()

def getSafeInput(message, list):
    response = input('\n'+message)
    if response.upper() not in list:
        pretty_print = ""
        for elem in list:
            if list.index(elem) > 0:
                pretty_print += ", "
            pretty_print += elem.lower()
        print("Please enter one of the following responses:",pretty_print)
        return getSafeInput(message, list)
    else: 
        return response

def getInput():
    new = input("Enter your list here: ")
    return new.split(", ")

def checkInput():
    new_list = getInput()
    print("Does this look right?")
    for item in new_list:
        print(f"- {item}")
    answer = input("y/n: ").upper()
    if answer == 'N':
        print("Let's try again!")
        return checkInput()
    elif answer == "Y":
        return new_list
    else:
        print("Sorry, I didn't understand that. Please re-enter your list.")
        return checkInput()