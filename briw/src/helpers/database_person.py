import briw.src.helpers.database_base as db
from briw.src.helpers.person_class import Person

def _insert_person_row(person: Person):
    values_string = f"({person.person_id},{person.first_name},{person.surname},{person.slack_id})"
    query = "INSERT INTO people (person_id, first_name, surname, slack_id) VALUES" + values_string
    db._insert_row(query)

def _parse_person_row(row):
    person_id = row[0]
    first_name = row[1]
    surname = row[2]
    slack_id = row[3]
    person = Person(person_id, first_name, surname, slack_id)
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

def get_person(person_id:int):
    try:
        query = "SELECT * FROM people WHERE person_id =",person_id
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