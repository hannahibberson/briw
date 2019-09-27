import src.helpers.database_base as db
from src.helpers.drink_class import Drink

def _insert_drink_row(drink: Drink):
    values_string = f'("{drink.name}","{drink.type}")'
    query = "INSERT INTO drinks (drink_name,drink_type) VALUES" + values_string
    db._insert_row(query)

def _parse_drink_row(row):
    drink_name = row[0]
    drink_type = row[1]
    drink = Drink(drink_name, drink_type)
    return drink

def get_drinks():
    drinks = []
    try:
        results = db._fetch_table('drinks')
        for row in results:
            drink = _parse_drink_row(row)
            drinks.append(drink)
    except:
        print("Connection Error.")
    return drinks

def get_drink(drink_name:str):
    try:
        query = f"SELECT * FROM drinks WHERE drink_name=\"{drink_name}\""
        results = db._query_database(query)
        if len(results) == 1:
            drink = _parse_drink_row(results[0])
            return drink
        else:
            print("There was no drink found with this name.")
    except:
        print("Connection Error.")

def add_drink(drink: Drink):
    _insert_drink_row(drink)