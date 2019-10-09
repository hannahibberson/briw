import briw.src.database_drink as drink_db
from briw.src.drink_class import Drink

def get_drinks():
    return drink_db.get_drinks()

def get_drink(drink_name):
    if len(drink_name) > 0:
        return drink_db.get_drink(drink_name)
    else:
        raise Exception("Not a valid drink name.")

def add_drink(data):
    drink = Drink(data["drink_name"])
    drink_db.add_drink(drink)