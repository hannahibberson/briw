import helpers.strings as strings
from helpers.menu_base import Menu, MenuOption
from helpers.menu_help import HelpMenu
from helpers.menu_people import PeopleMenu

class PeopleOption(MenuOption):
    def __init__(self):
        super(PeopleOption, self).__init__(strings.people_menu)

    def execute(self):
        people_menu = PeopleMenu()
        return people_menu.run()

class DrinkOption(MenuOption):
    def __init__(self):
        super(DrinkOption, self).__init__(strings.drinks_menu)

    def execute(self):
        pass

class FavouritesOption(MenuOption):
    def __init__(self):
        super(FavouritesOption, self).__init__(strings.favourites_menu)

    def execute(self):
        pass

class RoundsOption(MenuOption):
    def __init__(self):
        super(RoundsOption, self).__init__(strings.rounds_menu)

    def execute(self):
        pass

class HelpOption(MenuOption):
    def __init__(self):
        super(HelpOption, self).__init__(strings.get_help)

    def execute(self):
        help_menu = HelpMenu()
        return help_menu.run()

class ExitMainOption(MenuOption):
    def __init__(self):
        super(ExitMainOption, self).__init__(strings.exit_)

    def execute(self):
        print("Thank you for using this application! Goodbye.")
        exit()

class MainMenu(Menu):
    def __init__(self):
        
        people_menu = PeopleOption()
        drink_menu = DrinkOption()
        favourites_menu = FavouritesOption()
        rounds_menu = RoundsOption()
        help_ = HelpOption()
        exit_ = ExitMainOption()

        options = [people_menu, drink_menu, favourites_menu, rounds_menu, help_, exit_]

        super(MainMenu, self).__init__(options, strings.main_menu_context)