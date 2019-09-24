import briw.src.helpers.strings as strings
from briw.src.helpers.menu_base import Menu, MenuOption, ExitOption

class ShowPeopleOption(MenuOption):
    def __init__(self):
        super(ShowPeopleOption, self).__init__(strings.show_people)

    def execute(self):
        pass

class AddPeopleOption(MenuOption):
    def __init__(self):
        super(AddPeopleOption, self).__init__(strings.add_people)

    def execute(self):
        pass

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