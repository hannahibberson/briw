import strings
import user_input
import screen

def create_uuid(name, items):
    string = name[0:2]
    count = 0
    for item in items:
        if string in item:
            count += 1
    uuid = string + str(count)
    return uuid

def listAppend(name, items):
    name = name.lower()
    uuid = create_uuid(name, items)
    items[uuid] = {"uuid": uuid, "name":name}
    return items

def listRemove(uuid, items):
    if items[uuid]:
        items[uuid] = "REMOVED"
    else:
        raise Exception("Could not remove non-existent item")
    return items

def editList(title, data):
    if len(data[title]) > 0:
        response = user_input.getSafeInput(f"Would you like to ADD or REMOVE {title} from the list? ", ["ADD","REMOVE", "QUIT"])
        response = response.upper()
        if response == "QUIT":
            return
    else:
        response = "ADD"
    screen.clear()
    if response == "REMOVE":
        screen.printUuid(title, data[title])
    print(strings.list_edit(title, response))
    new_list = user_input.checkInput()
    if response == "ADD":
        for new in new_list:
            data[title] = listAppend(new, data[title])
    else:
        errors = []
        for new in new_list:
            try:
                data[title] = listRemove(new, data[title])
            except:
                errors.append(new)
        if len(errors) > 0:
            print("The following could not be removed:", ', '.join(errors))
    return data

def checkLists(data):
    data["people"] = checkList("people", data)
    data["drinks"] = checkList("drinks", data)
    return data

def checkList(title, data):
    exist = 0
    for uuid, value in data[title].items():
        if not value == "REMOVED":
            exist += 1
    if exist == 0:
        return {}
    else:
        return data[title]
