class Person:
    def __init__(self, person_id, first_name, surname, slack_id):
        self.person_id = person_id
        self.first_name = first_name
        self.surname = surname
        self.slack_id = slack_id

class Drink:
    def __init__(self, drink_name, drink_type):
        self.name = drink_name
        self.type = drink_type

class Preference:
    def __init__(self, person_id, drink_id, options = ""):
        self.person_id = person_id
        self.drink_id = drink_id
        self.options = options
