import os
import strings

def clear():
    os.system("clear")

def getMenus(people_length, drinks_length):
    menu_items = []
    help_items = []
    if people_length == 0:
        menu_items.append(strings.edit_people)
        help_items.append(strings.edit_people_help)
    else:
        menu_items.extend([strings.get_people, strings.edit_people])
        help_items.extend([strings.get_people_help, strings.edit_people_help])
    if drinks_length == 0:
        menu_items.append(strings.edit_drinks)
        help_items.append(strings.edit_drinks_help)
    else:
        menu_items.extend([strings.get_drinks, strings.edit_drinks])
        help_items.extend([strings.get_drinks_help, strings.edit_drinks_help])
    if people_length > 0 and drinks_length > 0:
        help_items.append(strings.favourites_help)
        menu_items.append(strings.favourites)
    menu_items.extend([strings.get_help, strings.exit_])
    help_items.extend([strings.help_help, strings.exit_help])
    return menu_items, help_items

def printMenu(items, type):
    if type == "help":
        print(strings.help_context,'\n')
    else:
        print(strings.menu_context,'\n')
    for item in items:
        identifier = items.index(item) + 1
        print(" ",identifier,item)

def returnMenu():
    input('\n'+strings.menu_return)

def printList(title, arr):
    width = tableWidth(arr)
    if width > 40:
        width = 40
    divider = '-'*width
    pre_space = ' '*int((width-len(title))/2)
    print(divider+"\n"+pre_space+title.upper()+"\n"+divider)
    rows = 0
    for uuid in arr:
        item = arr[uuid]
        if not item == "REMOVED":
            rows += 1
            name = item["name"].capitalize()
            for i in range(int(len(name)/38)+1):
                start_index = i*38
                symbol = ' '
                if i == 0:
                    keys = list(arr.keys())
                    for key in keys:
                        if arr[key] == "REMOVED":
                            keys.remove(key)
                    symbol = keys.index(uuid) + 1
                print(symbol, name[start_index:start_index+38])
    
    if rows == 0:
        print(f"There are currently no {title.lower()} stored.")
    print(divider)

def printUuid(title, list):
    print(title.upper())
    for key in list:
        item = list[key]
        if not item == "REMOVED":
            print(item["uuid"],item["name"])

def tableWidth(list):
    max_length = 0
    for uuid in list:
        element = list[uuid]
        if not element == "REMOVED":
            if len(element["name"]) > max_length:
                max_length = len(element["name"])
    return (max_length+2)