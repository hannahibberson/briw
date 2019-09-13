import os

def readFile(filename):
    if not os.path.isfile(filename):
        file = open(filename, "w")
    file = open(filename, "r")
    arr = file.read().splitlines()
    file.close()
    return arr

def storePeople():
    arr = readFile("people.txt")
    people = {}
    for person in arr:
        person = person.split(';')
        uuid = person[0]
        name = person[1]
        favourites = person[2].split(',')
        people[uuid] = {"uuid":uuid, "name":name, "favourites":favourites}
    return people

def storeDrinks():
    arr = readFile("drinks.txt")
    drinks = {}
    for drink in arr:
        drink = drink.split(';')
        uuid = drink[0]
        name = drink[1]
        drinks[uuid] = {"uuid":uuid, "name":name}
    return drinks

def storeRound():
    pass

def store():
    people = storePeople()
    drinks = storeDrinks()
    return {"people":people, "drinks":drinks}

def writeFile(filename,arr):
    file = open(filename,"w")
    for item in arr:
        file.write(item+'\n')
    file.close()

def writePeople(people):
    arr = []
    for uuid in people:
        person = people[uuid]
        if not person == "REMOVED":
            try:
                favourites = ','.join(person["favourites"])
            except:
                favourites = ""
            string = person["uuid"]+";"+person["name"]+";"+favourites
            arr.append(string)
    writeFile("people.txt",arr)

def writeDrinks(drinks):
    arr = []
    for uuid in drinks:
        drink = drinks[uuid]
        if not drink == "REMOVED":
            string = drink["uuid"]+";"+drink["name"]
            arr.append(string)
    writeFile("drinks.txt",arr)

def write(data):
    writePeople(data["people"])
    writeDrinks(data["drinks"])