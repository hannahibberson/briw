class Store:
    def __init__(self):
        # pull in stuff from files

    def get_people():
        return self.people

    def get_active_people():
        tmp = {}
        for uuid, user_info in getPeople():
            if user_info["isActive"] == True:
                tmp[uuid] = user_info
        return tmp

    def getPerson(uuid):
        return getPeople()[uuid]

    def getPersonName(uuid):
        return getPerson(uuid)["name"]

    def getFavourites(uuid):
        return getPerson(uuid)["favourites"]

    def getUserUuids(name):
        return getUuids(name, getPeople())

    def getDrinks():
        return store["drinks"]

    def getDrink(uuid):
        return getDrinks()[uuid]

    def getDrinkName(uuid):
        return getDrink(uuid)["name"]

    def getDrinkUuids(name):
        return getUuids(name, getDrinks())
        
    def getUuids(name,array):
        uuids = []
        for uuid, info in array:
            if info["name"] == name:
                uuids.append(uuid)
        return uuids

    def setPeople(people):
        store["people"] = people

    def setPerson(uuid,person):
        store["people"][uuid] = person

    def setPersonFavourites(uuid,favourites):
        store["people"][uuid]["favourites"] = favourites

    def setPersonInactive(uuid):
        store["people"][uuid]["isActive"] = False

    def setDrinks(drinks):
        store["drinks"] = drinks

    def setDrink(uuid,drink):
        store["drinks"][uuid] = drink
