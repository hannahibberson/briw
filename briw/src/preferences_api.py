import briw.src.database_preference as pref_db

def get_favourites():
    return pref_db.get_preferences()

def get_favourite(person_id_str: str):
    if len(person_id_str) > 0 and person_id_str.isdigit():
        return pref_db.get_preference(int(person_id_str))
    else:
        raise Exception("Not a valid number.")

def change_favourite(data):
    person_id = int(data["person_id"])
    drink_name = data["drink_name"]
    pref_db.add_preference(person_id,drink_name)