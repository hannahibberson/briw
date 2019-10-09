import briw.src.database_person as person_db
from briw.src.person_class import Person

def get_people():
    return person_db.get_people()

def parse_people_query(query):
    if 'id=' in query:
        person_id = query.split("=")[1]
        return get_person_by_id(person_id)
    else:
        return get_person_by_names(query)

def get_person_by_id (person_id):
    if len(person_id) > 0 and person_id.isdigit():
        return person_db.get_person_by_id(person_id)
    else:
        raise Exception("Not a valid number.")

def get_person_by_names(query_string):
    arguments = query_string.split("&")
    first_name = arguments[0]
    surname = arguments[1]
    slack_id = arguments[2]
    if len(first_name) > 0 and len(surname) > 0 and len(slack_id) > 0:
        return person_db.get_person_by_names(first_name, surname, slack_id)
    else:
        raise Exception("Not a valid set of arguments")

def add_person(data):
    person = Person(data["first_name"], data["surname"], data["slack_id"])
    person_db.add_person(person)