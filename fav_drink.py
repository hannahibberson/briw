import sys
import os
import briw.src.helpers.strings as strings

os.system("clear")
store = {}

def main():
    store["people"] = readFile("old_people.txt")
    store["drinks"] = readFile("old_drinks.txt")
    store["favourites"] = readFavourites()
    while True:
        main_menu, help_menu = dynamicMenu()
        printMenu(main_menu, "main")
        command = get_command()
        command_string = main_menu[command-1]
        if command_string == strings.exit_:
            os.system("clear")
            print("See you again soon!")
            writeFiles()
            exit()
        if command_string == strings.get_help:
            os.system("clear")
            printMenu(help_menu, "help")
            return_menu()
        elif command_string == strings.get_people:
            printList("people", store["people"])
            return_menu()
        elif command_string == strings.get_drinks:
            printList("drinks", store["drinks"])
            return_menu()
        elif command_string == strings.favourites:
            checkConnections()
        elif command_string == strings.edit_people:
            listEdit('people', store["people"])
        elif command_string == strings.edit_drinks:
            listEdit('drinks', store["drinks"])
        os.system("clear")

def readFile(name):
    if not os.path.isfile(name):
        file = open(name, "w")
    file = open(name, "r")
    arr = file.read().splitlines()
    file.close()
    return arr

def readFavourites():
    arr = readFile("old_favourites.txt")
    tmp_dict = {}
    for pair in arr:
        tmp = pair.split(',')
        tmp_dict[tmp[0]] = tmp[1]
    return tmp_dict

def writeFiles():
    writeFile("people")
    writeFile("drinks")
    writeFavourites() 

def writeFile(name):
    filename = "old_"+name+".txt"
    file = open(filename,"w")
    for item in store[name]:
        file.write(item+'\n')
    file.close()

def writeFavourites():
    file = open("old_favourites.txt","w")
    favourites = []
    for name,drink in store["favourites"].items():
        string = name+","+drink
        favourites.append(string)
    for item in favourites:
        file.write(item+'\n')
    file.close()

def dynamicMenu():
    menu_items = []
    help_items = []
    if len(store["people"]) == 0:
        menu_items.append(strings.edit_people)
        help_items.append(strings.edit_people_help)
    else:
        menu_items.extend([strings.get_people, strings.edit_people])
        help_items.extend([strings.get_people_help, strings.edit_people_help])
    if len(store["drinks"]) == 0:
        menu_items.append(strings.edit_drinks)
        help_items.append(strings.edit_drinks_help)
    else:
        menu_items.extend([strings.get_drinks, strings.edit_drinks])
        help_items.extend([strings.get_drinks_help, strings.edit_drinks_help])
    if len(store["people"]) > 0 and len(store["drinks"]) > 0:
        help_items.append(strings.favourites_help)
        menu_items.append(strings.favourites)
    menu_items.extend([strings.get_help, strings.exit_])
    help_items.extend([strings.help_help, strings.exit_help])
    return menu_items, help_items

def get_command():
    command = input("\nOption number: ")
    try:
        return int(command)
    except:
        print("Please enter an integer value from the list above.")
        return get_command()

def printMenu(menu_items, menu_type):
    if menu_type == "help":
        print(strings.help_context,'\n')
    else:
        print(strings.menu_context,'\n')
    for item in menu_items:
        identifier = menu_items.index(item) + 1
        print(" ",identifier,item)

def return_menu():
    input('\n'+strings.menu_return)

def printList(title, arr):
    width = tableWidth(arr)
    if width > 40:
        width = 40
    divider = '-'*width
    pre_space = ' '*int((width-len(title))/2)
    print(divider+"\n"+pre_space+title.upper()+"\n"+divider)
    if len(arr) == 0:
        print(f"There are currently no {title} stored.")
    else:
        for item in arr:
            for i in range(int(len(item)/38)+1):
                start_index = i*38
                symbol = ' '
                if i == 0:
                    symbol = arr.index(item) + 1
                print(symbol, item[start_index:start_index+38])
    print(divider)

def tableWidth(arr):
    max_length = 0
    for element in arr:
        if len(element) > max_length:
            max_length = len(element)
    return (max_length+2)

def listEdit(title, arr):
    if len(store[title]) > 0:
        response = input(f"Would you like to ADD or REMOVE {title} from the list? ")
    else:
        response = "ADD"
    if response.upper() == "ADD":
        listAppend(title, arr)
        writeFile(title)
    elif response.upper() == "REMOVE":
        listRemove(title, arr)
        writeFile(title)
    else:
        print("I'm sorry, I don't understand! Please enter either 'ADD' or 'REMOVE'.")
        listEdit(title, arr)

def listAppend(title, arr):
    print(f"""
ADDING NEW {title.upper()}
--------------------
Please enter your list separated by commas. For example:
    a, b, c
To make no changes, please press 'enter'.
    """)
    valid = False
    while valid == False:
        new_list = getInput()
        if len(new_list[0]) > 0:
            valid = checkInput(new_list)
        else: 
            valid = True
    
    length = len(arr)
    if len(new_list[0]) > 0:
        arr += new_list
    if len(arr) == length:
        print("No changes to the list!")
        return_menu()
    else:
        os.system("clear")
        print("Here's the updated list:")
        printList(title, arr)
        return_menu()

def listRemove(title, arr):
    print(f"""
REMOVING {title.upper()}
--------------------
Please enter a list of {title} to remove separated by commas. For example:
    a, b, c
To make no changes, please press 'enter'.
    """)
    valid = False
    while valid == False:
        new_list = getInput()
        if len(new_list[0]) > 0:
            valid = checkInput(new_list)
        else: 
            valid = True
    
    errors = []
    length = len(arr)
    if len(new_list[0]) > 0:
        for item in new_list:
            if item in arr:
                arr.remove(item)
            else:
                errors.append(item)
    os.system("clear")
    if len(errors) > 0:
        print(f"Please note, we were unable to remove:")
        for error in errors:
            print(f"- {error}")
        print("-----------------")
    if len(arr) == length:
        print("No changes were made!")
        return_menu()
    else:
        print("Here's the updated list:")
        printList(title, arr)
        return_menu()
    

def getInput():
    new = input("Enter your list here: ")
    return new.split(", ")

def checkInput(new_list):
    print("Does this look right?")
    for item in new_list:
        print(f"- {item}")
    answer = input("y/n: ").upper()
    if answer == 'N':
        print("Let's try again!")
        return False
    elif answer == "Y":
        return True
    else:
        print("Sorry, I didn't understand that. Please re-enter your list.")
        return False

def checkConnections():
    choice = input("Would you like to VIEW or EDIT the list of people's favourite drinks? ")
    if choice.upper() == "VIEW":
        printConnections()
    elif choice.upper() == "EDIT":
        connect()
    else: 
        print("I'm not sure what that means, please enter 'VIEW' or 'EDIT'.")
        checkConnections()

def connect():
    printList('people', store["people"])
    person_num = getNumber("Enter the number of the person you would like to assign a favourite drink: ", len(store["people"]))
    name = store["people"][person_num]
    printList('drinks', store["drinks"])
    drink_message = "Enter the number of "+name+"'s favourite drink: "
    drink_num = getNumber(drink_message, len(store["drinks"]))
    drink = store["drinks"][drink_num]
    store["favourites"][name] = drink
    valid = checkConnection(name, drink)
    if valid == True:
        writeFavourites()
        printConnections()
    else:
        print("Okay, let's restart")
        connect()

def checkConnection(name, drink):
    print(f"You would like to set {name}'s favourite drink to {drink}.")
    valid = False
    while valid == False:
        response = input("Is this correct? y/n")
        if response.upper() == "Y":
            valid = True
            return True
        elif response.upper() == "N":
            valid = True
            return False
        else:
            print("I didn't understand that, let's try again!")
            checkConnection(name, drink)

def getNumber(message, range):
    response = input(message)
    if len(response) == 0:
        print("Please enter a number.")
        return getNumber(message, range)
    elif int(response) > 0 and int(response) <= range:
        return int(response) - 1
    else:
        print(f"Please enter a number no larger than {range}")
        return getNumber(message, range)

def printConnections():
    os.system('clear')
    print("Here's the current list of favourite drinks:\n")
    if len(store["favourites"].items()) == 0:
        print("There are currently no favourites set.")
    else:
        for name, drink in store["favourites"].items():
            print(f"| {name}'s favourite drink is {drink}")
    return_menu()
main()
