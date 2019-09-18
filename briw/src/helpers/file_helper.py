import os
import briw.src.helpers.convert_data as convert

### Functions to access the files ###

def check_file_exists(filename):
    if not os.path.isfile(filename):
        _create_file(filename)

def _create_file(filename):
    file = open(filename, "w")
    file.close()

def _read_file_lines(filename):
    check_file_exists(filename)
    file = open(filename, "r")
    lines_list = file.read().splitlines()
    file.close()
    return lines_list

def _write_to_file(filename, lines_to_write):
    check_file_exists(filename)
    file = open(filename,"w")
    for line in lines_to_write:
        file.write(line+'\n')
    file.close()

### Functions for handling the data ###

def _get_filename(data_type):
    if data_type == "people":
        return "people.txt"
    elif data_type == "drinks":
        return "drinks.txt"
    elif data_type == "preferences":
        return "preferences.txt"


def _get_objects_from_strings(strings_to_convert, data_type):
    objects = []
    for string in strings_to_convert:
        obj = convert.string_to_object(string, data_type)
        objects.append(obj)
    return objects

def _get_state_from_file(data_type):
    filename = _get_filename(data_type)
    state_as_strings = _read_file_lines(filename)
    state = _get_objects_from_strings(state_as_strings, data_type)
    return state

def _get_strings_from_objects(objects_to_convert, data_type):
    strings = []
    for obj in objects_to_convert:
        string = convert.stringify_object(obj, data_type)
        strings.append(string)
    return strings

def _write_state_to_file(data_list, data_type):
    state_as_strings = _get_strings_from_objects(data_list, data_type)
    filename = _get_filename(data_type)
    _write_to_file(filename, state_as_strings)


### Functions for specific datatypes ###

def read_people_from_file():
    return _get_state_from_file("people")

def write_people_to_file(people_list):
    return _write_state_to_file(people_list, "people")

def read_drinks_from_file():
    return _get_state_from_file("drinks")

def write_drinks_to_file(drink_list):
    return _write_state_to_file(drink_list, "drinks")

def read_preferences_from_file():
    return _get_state_from_file("preference")

def write_preferences_to_file(preference_list):
    return _write_state_to_file(preference_list, "preferences")
