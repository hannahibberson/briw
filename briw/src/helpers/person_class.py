class Person:
    def __init__(self, person_id, first_name, surname, slack_id):
        self.person_id = person_id

        self.first_name = first_name
        self.surname = surname
        self.name = first_name,surname
        
        self.slack_id = slack_id
