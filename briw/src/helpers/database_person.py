import src.helpers.database_base as db
from src.helpers.person_class import Person

def _insert_person_row(person: Person):
    values_string = f"('{person.first_name}','{person.surname}','{person.slack_id}')"
    query = "INSERT INTO people (first_name, surname, slack_id) VALUES "+ values_string
    db._insert_row(query)
    print(f"{person.name.title()} added!")

def _parse_person_row(row):
    person_id = row[0]
    first_name = row[1]
    surname = row[2]
    slack_id = row[3]
    person = Person(first_name, surname, slack_id, person_id)
    return person

def get_people():
    people = []
    try:
        results = db._fetch_table('people')
        for row in results:
            person = _parse_person_row(row)
            people.append(person)
    except:
        print("Connection Error.")
    return people

def get_person_by_id(person_id:int):
    try:
        query = "SELECT * FROM people WHERE person_id = "+str(person_id)
        results = db._query_database(query)
        if len(results) == 1:
            person = _parse_person_row(results[0])
            return person
        else:
            print("There was no-one found that matched your query.")
    except:
        print("Connection Error.")

def get_person_by_names(first_name:str,surname:str,slack_id:str):
    try:
        query = f'SELECT * FROM people WHERE first_name="{first_name}" AND surname="{surname}" AND slack_id="{slack_id}"'
        print(query)
        results = db._query_database(query)
        if len(results) == 1:
            person = _parse_person_row(results[0])
            return person
        else:
            print("There was no-one found that matched your query.")
    except:
        print("Connection Error.")

def add_person(person: Person):
    _insert_person_row(person)