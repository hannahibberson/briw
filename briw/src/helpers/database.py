import pymysql
import briw.src.helpers._db_connect as db
from os import environ

from briw.src.helpers.classes import Person, Drink

def _connect_to_database():
    my_database = pymysql.connect(
        db._host,
        db._username,
        db._password,
        db._database
    )
    return my_database

def _close_database(database):
    database.close()

def _fetch_table(table_name: str):
    db = _connect_to_database()
    cursor = db.cursor()
    query = "SELECT * FROM " + table_name
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results

def _query_database(query: str, returns_result: bool = True):
    db = _connect_to_database()
    cursor = db.cursor()
    cursor.execute(query)
    if returns_result == True:
        results = cursor.fetchall()
    db.close()
    if returns_result == True:
        return results

def _insert_row(query: str):
    _query_database(query, False)

def _insert_person_row(person: Person):
    values_string = f"({person.person_id},{person.first_name},{person.surname},{person.slack_id})"
    query = "INSERT INTO people (person_id, first_name, surname, slack_id) VALUES" + values_string
    _insert_row(query)
    
def _insert_drink_row(drink: Drink):
    values_string = f"({drink.drink_name},{drink.drink_type})"
    query = "INSERT INTO drinks (drink_name,drink_type) VALUES" + values_string
    _insert_row(query)

def _parse_person_row(row):
    person_id = row[0]
    first_name = row[1]
    surname = row[2]
    slack_id = row[3]
    person = Person(person_id, first_name, surname, slack_id)
    return person

def _parse_drink_row(row):
    drink_name = row[0]
    drink_type = row[1]
    drink = Drink(drink_name, drink_type)
    return drink

def get_people():
    people = []
    try:
        results = fetch_table('people')
        for row in results:
            person = parse_person_row(row)
            people.append(person)
    except:
        print("Connection Error.")
    return people

def get_person(person_id):
    try:
        query = "SELECT * FROM people WHERE person_id =",person_id
        results = _query_database(query)
        if len(results) == 1:
            person = parse_person_row(results[0])
            return person
        elif len(results) > 1:
            print("There was more than one person found with this person_id.")
        else:
            print("There was no-one found with this person_id")
    except:
        print("Connection Error.")


def add_person(person: Person):
    _insert_person_row(person)

def get_drinks():
    drinks = []
    try:
        results = fetch_table('drinks')
        for row in results:
            drink = parse_drink_row(row)
            drinks.append(drink)
    except:
        print("Connection Error.")
    return drinks

def add_drink(drink: Drink):
    _insert_drink_row(drink)