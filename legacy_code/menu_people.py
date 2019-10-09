import helpers.strings as strings
import helpers.user_input as u_input
from helpers.menu_base import Menu, MenuOption, ExitOption
from helpers.person_class import Person
import helpers.database_person as person_db
#import briw.src.helpers.pretty_print as p_print


class ShowPeopleOption(MenuOption):
    def __init__(self):
        super(ShowPeopleOption, self).__init__(strings.show_people)

    def execute(self):
        pass

class AddPeopleOption(MenuOption):
    def __init__(self):
        super(AddPeopleOption, self).__init__(strings.add_people)

    def string_validation(self,string):
        print(string)
        if string.isdigit() == False and len(string) > 0:
            return True
        else:
            return False

    def get_user_details_input(self):
        first_name_prompt = "What is the first name of the new user? "
        first_name = u_input.user_input(self.string_validation,first_name_prompt).lower()
        surname_prompt = "What is the user's surname? "
        surname = u_input.user_input(self.string_validation,surname_prompt).lower()
        slackid_prompt = "What is the user's slackid? "
        slackid = u_input.user_input(self.string_validation,slackid_prompt).lower()

        person = Person(first_name,surname,slackid)
        return person

    def check_user_details(self, person:Person):
        print("You are adding the following person:")
        print(f"{person.name.title()} and their slack id is {person.slack_id}")
        return u_input.get_user_choice_confirmation("Does this look right? y/n: ")

    def get_and_add_user_details(self):
        continue_check = True
        user_added = False
        while continue_check == True:
            person = self.get_user_details_input()
            valid_person = self.check_user_details(person)
            if valid_person == True:
                continue_check = False
                self.add_user_to_database(person)
                user_added = True
            else:
                continue_check = u_input.get_user_choice_confirmation("Would you like to try and enter the user details again? y/n: ")
        return user_added

    def add_user_to_database(self,person:Person):
        person_db.add_person(person)

    def execute(self):
        more_people = True
        change_made = False
        while more_people == True:
            user_added = self.get_and_add_user_details()
            if user_added:
                change_made = True
            more_people = u_input.get_user_choice_confirmation("Would you like to add another person? y/n: ")
        if change_made == True:
            print("Your list of registered users now looks like this:")
            #p_print.print_people()
        else:
            print("No changes were made.")
        u_input.get_input("Press enter to return to the main menu.")

class RemovePeopleOption(MenuOption):
    def __init__(self):
        super(RemovePeopleOption, self).__init__(strings.remove_people)

    def execute(self):
        pass

class PeopleMenu(Menu):
    def __init__(self):
        
        show_people = ShowPeopleOption()
        add_people = AddPeopleOption()
        remove_people = RemovePeopleOption()
        exit_ = ExitOption()

        options = [show_people, add_people, remove_people, exit_]

        super(PeopleMenu, self).__init__(options, strings.people_menu_context)