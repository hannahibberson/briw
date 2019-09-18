# TODO: re-do this file and consider what we want to store and how we want to store it 
#   (i.e. probably best to be a module not a class? otherwise how do we only keep one store and get it between the functions?)
class Store:
    def __init__(self):
        # pull in stuff from files
        self.people = []
        self.drinks = []
        self.preferences = []

    def get_people(self):
        return self.people

    def get_active_people(self):
        tmp = {}
        for uuid, user_info in self.get_people():
            if user_info["isActive"] == True:
                tmp[uuid] = user_info
        return tmp

    def getPerson(self,uuid):
        return self.get_people()[uuid]

    def getPersonName(self,uuid):
        return self.getPerson(uuid)["name"]

    def getFavourites(self,uuid):
        return self.getPerson(uuid)["favourites"]

    def getUserUuids(self,name):
        return self.getUuids(name, self.get_people())

    def getDrinks(self):
        return self.drinks

    def getDrink(self,uuid):
        return self.getDrinks()[uuid]

    def getDrinkName(self,uuid):
        return self.getDrink(uuid)["name"]

    def getDrinkUuids(self,name):
        return self.getUuids(name, self.getDrinks())
        
    def getUuids(self,name,array):
        uuids = []
        for uuid, info in array:
            if info["name"] == name:
                uuids.append(uuid)
        return uuids

    def setPeople(self,people):
        self.people = people

    def setPerson(self,uuid,person):
        self.people[uuid] = person

    def remove_person(self, uuid):
        # Remove a person
        # Will also need to remove them from preferences
        pass

    def setPersonFavourites(self,uuid,favourites):
        self.people[uuid]["favourites"] = favourites

    def setPersonInactive(self,uuid):
        self.people[uuid]["isActive"] = False

    def setDrinks(self,drinks):
        self.drinks = drinks

    def setDrink(self,uuid,drink):
        self.drinks[uuid] = drink

    def removeDrink(self,drink_id):
        # Remove a drink
        # Will also need to remove them from preferences 
        pass
