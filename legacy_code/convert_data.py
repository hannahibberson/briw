from briw.src.helpers.classes import Person, Drink, Preference

### General functions ###

def _split_string_into_list(string):
    return string.split(";")

def string_to_object(string_to_objectify, data_type):
    object_elements = _split_string_into_list(string_to_objectify)
    if data_type == "people":
        return _string_to_person(object_elements) 
    elif data_type == "drinks":
        return _string_to_drink(object_elements)
    elif data_type == "preferences":
        return _string_to_preference(object_elements)

def stringify_object(object_to_stringify, data_type):
    if data_type == "people":
        return _stringify_person(object_to_stringify)
    elif data_type == "drinks":
        return _stringify_drink(object_to_stringify)
    elif data_type == "preferences":
        return _stringify_preference(object_to_stringify)

### Person specific functions ###

def _string_to_person(string_list):
    first_name = string_list[0]
    surname = string_list[1]
    slack_id = string_list[2]
    person = Person(first_name, surname, slack_id)
    return person

def _stringify_person(person):
    return f"{person.first_name};{person.surname};{person.slack_id}"

### Drink specific functions ###

def _string_to_drink(string_list):
    drink_name = string_list[0]
    drink_type = string_list[1]
    drink = Drink(drink_name, drink_type)
    return drink

def _stringify_drink(drink):
    return f"{drink.name};{drink.type}"

### Preference specific functions ###

def _string_to_preference(string_list):
    person_id = string_list[0]
    drink_id = string_list[1]
    options = string_list[2]
    preference = Preference(person_id, drink_id, options)
    return preference

def _stringify_preference(preference):
    return f"{preference.person_id};{preference.drink_id};{preference.options}"
