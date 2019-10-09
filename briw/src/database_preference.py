import briw.src.database_base as db

def _insert_preference_row(person_id: int, drink_name: str):
    values_string = f'({person_id},"{drink_name}")'
    query = "INSERT INTO preferences (person_id,drink_name) VALUES" + values_string
    db._insert_row(query)

def get_preferences():
    preferences = {}
    try:
        results = db._fetch_table('preferences')
        for row in results:
            person_id = row[0]
            drink_name = row[1]
            preferences[person_id] = drink_name
    except:
        print("Connection Error.")
    return preferences

def get_preference(person_id:int):
    try:
        query = "SELECT drink_name FROM preferences WHERE person_id="+str(person_id)
        results = db._query_database(query)
        if len(results) == 1:
            drink_name = results[0][0]
            return drink_name
        else:
            print("There was no preference found for this person.")
    except:
        print("Connection Error.")

def alter_preference(person_id:int, drink_name:str):
    try:
        query = f"UPDATE preferences SET drink_name=\"{drink_name}\" WHERE person_id={str(person_id)}"
        db._query_database(query,False)
    except:
        print("Connection Error.")

def add_preference(person_id:int, drink_name:str):
    preference = get_preference(person_id)
    if preference:
        alter_preference(person_id, drink_name)
    else:
        _insert_preference_row(person_id, drink_name)

