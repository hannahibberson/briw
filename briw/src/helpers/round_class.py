'''
from src.helpers.person_class import Person
from src.helpers.drink_class import Drink

import src.helpers.database_preference as preference_db
import src.helpers.database_drink as drink_db
'''

class Round:
    def __init__(self, id: int, owner_id: int, active: bool, orders):
        self.id = id
        self.owner_id = owner_id
        self.active = active
        self.orders = orders

'''
    def start(self):
        print("A new round has started!")
        self.active = True

    def join_round(self, person: Person):
        if self.active == True:
            self.people.append(person)
            print(f"{person.name.capitalize()} has been added to the current round.")
        else:
            print("Sorry, there's currently no round active!")

    def leave_round(self, person: Person):
        self.people.remove(person)
        print(f"{person.name.capitalize()} has been removed from the current round.")

    def end(self):
        print("The round has been closed.")
        self.active = False
        print("\n-----------------------\nYou need to make:\n-----------------------")
        for drink_type, drinks in self.get_drinks().items():
            print(f"{drink_type.capitalize()}:")
            for drink, count in drinks.items():
                print(drink.name.capitalize(),'-',count)
        print("-----------------------\n")
        self.people = []

    def get_drinks(self):
        drinks = {}
        preferences = preference_db.get_preferences()
        for member in self.people:
            drink_name = preferences[member.person_id]
            try:
                drink: Drink = drink_db.get_drink(drink_name)
                if not drink.type in drinks.keys():
                    drinks[drink.type] = {}
                if not drink.name in drinks[drink.type].keys():
                    drinks[drink.type][drink.name] = 0
                drinks[drink.type][drink.name] += 1
            except:
                print("Couldn't fetch this preference.")
        return drinks
'''