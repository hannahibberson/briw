class Person:
    def __init__(self, first_name, surname, slack_id, person_id = None):
        self.person_id = person_id

        self.first_name = first_name
        self.surname = surname
        self.name = first_name + ' ' + surname
        
        self.slack_id = slack_id
